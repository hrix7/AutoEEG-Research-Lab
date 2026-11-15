"""Deterministic experiment runner. Python standard library only."""
import argparse
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import random
import statistics

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def encode(obj):
    return (json.dumps(obj, indent=2, sort_keys=True, allow_nan=False) + "\n").encode()

def table(rows):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerows(rows)
    return stream.getvalue().encode()

def mean(xs):
    return statistics.mean(xs)

def spectral_power(signal, fs, frequency, window="rectangular"):
    # One-sided periodogram at an integer DFT bin; units amplitude squared / Hz.
    n = len(signal)
    if n < 3 or not math.isfinite(fs) or fs <= 0 or not 0 < frequency < fs/2 or any(not math.isfinite(x) for x in signal):
        raise ValueError("finite signal of at least three samples and an interior positive frequency required")
    if window not in ("rectangular", "hann"):
        raise ValueError("window must be rectangular or hann")
    offset = mean(signal)
    weights = [1.0]*n if window == "rectangular" else [.5-.5*math.cos(2*math.pi*i/(n-1)) for i in range(n)]
    centered = [(x - offset)*w for x,w in zip(signal,weights)]
    re = sum(x * math.cos(2 * math.pi * frequency * i / fs) for i, x in enumerate(centered))
    im = sum(x * math.sin(2 * math.pi * frequency * i / fs) for i, x in enumerate(centered))
    return 2 * (re * re + im * im) / (fs * sum(w*w for w in weights))

def signal_epoch(rng, fs, seconds, alpha, noise, artifact):
    xs = [alpha * math.sin(2 * math.pi * 10 * i / fs)
          + 4 * math.sin(2 * math.pi * 20 * i / fs)
          + rng.gauss(0, noise) for i in range(fs * seconds)]
    if artifact:
        for i in range(fs // 2, fs // 2 + 8):
            xs[i] += 250
    return xs

def off_bin_probe(fs, seconds, frequency=10.3):
    if type(fs) is not int or type(seconds) is not int or fs<82 or seconds<1 or not math.isfinite(frequency) or not 0<frequency<fs/2:
        raise ValueError('positive duration, integer fs>=82 and interior positive frequency required')
    samples=[math.sin(2*math.pi*frequency*i/fs) for i in range(fs*seconds)]
    estimates=[]
    for window in ('rectangular','hann'):
        powers={f:spectral_power(samples,fs,f,window) for f in range(1,41)}
        peak=max(powers,key=powers.get)
        total=sum(powers.values())
        estimates.append(dict(window=window,peak_hz=peak,absolute_peak_error_hz=abs(peak-frequency),far_grid_fraction=sum(v for f,v in powers.items() if abs(f-frequency)>2)/total))
    return dict(generator_frequency_hz=frequency,amplitude=1,noise_sd=0,grid_hz=list(range(1,41)),estimates=estimates,interpretation='Noiseless off-bin probe on the fixed integer-Hz evaluation grid; a fractional frequency is not recovered exactly and Hann suppression is not disease classification.')

def validate_config(config):
    for name,minimum in [('fs_hz',82),('seconds',1),('epochs_per_noise',1)]:
        if type(config.get(name)) is not int or config[name]<minimum:
            raise ValueError(name+' must be an integer >= '+str(minimum))
    if type(config.get('seed')) is not int:
        raise ValueError('seed must be an integer')
    for name in ('alpha_uV','peak_to_peak_limit_uV'):
        value=config.get(name)
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError(name+' must be finite and nonnegative')
    noise=config.get('noise_levels')
    if not isinstance(noise,list) or not noise or any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0 for v in noise) or len(set(noise))!=len(noise):
        raise ValueError('noise_levels must be unique finite nonnegative numbers')

def run(config):
    validate_config(config)
    rng = random.Random(config['seed'])
    rows = [['epoch', 'noise_sd_uV', 'artifact_injected', 'sample', 'amplitude_uV']]
    results = []
    for noise in config['noise_levels']:
        accepted, peaks, ratios, rejected, tp, injected = 0, [], [], 0, 0, 0
        hann_peaks, hann_ratios = [], []
        for epoch in range(config['epochs_per_noise']):
            artifact = epoch % 4 == 0
            injected += int(artifact)
            xs = signal_epoch(rng, config['fs_hz'], config['seconds'], config['alpha_uV'], noise, artifact)
            rows.extend([epoch, noise, int(artifact), i, format(x, '.12g')] for i, x in enumerate(xs))
            reject = max(xs) - min(xs) > config['peak_to_peak_limit_uV']
            rejected += reject
            tp += reject and artifact
            if not reject:
                powers = {f: spectral_power(xs, config['fs_hz'], f) for f in range(1, 41)}
                for window,peak_values,ratio_values in [('rectangular',peaks,ratios),('hann',hann_peaks,hann_ratios)]:
                    spectrum = powers if window=='rectangular' else {f:spectral_power(xs,config['fs_hz'],f,window) for f in range(1,41)}
                    total=sum(spectrum.values())
                    if total>0:
                        peak_values.append(max(spectrum,key=spectrum.get))
                        ratio_values.append(sum(v for f,v in spectrum.items() if 8<=f<=12)/total)
                accepted += 1
        results.append(dict(noise_sd_uV=noise, accepted=accepted, rejected=rejected,
                            artifact_true_positives=tp, artifact_injected=injected,
                            artifact_false_positives=rejected-tp,
                            artifact_false_negatives=injected-tp,
                            artifact_true_negatives=config['epochs_per_noise']-injected-(rejected-tp),
                            spectral_epochs=len(peaks),
                            hann_mean_peak_hz=mean(hann_peaks) if hann_peaks else None,
                            hann_mean_alpha_fraction=mean(hann_ratios) if hann_ratios else None,
                            mean_peak_hz=mean(peaks) if peaks else None,
                            mean_alpha_fraction=mean(ratios) if ratios else None))
    return rows, {'conditions': results, 'off_bin_probe':off_bin_probe(config['fs_hz'],config['seconds']), 'interpretation': 'Spectral recovery on generated sinusoids only; no disease labels or patient data.'}

def experiment():
    config = json.loads((ROOT / 'config.json').read_text())
    rows, metrics = run(config)
    data = table(rows)
    result = dict(schema_version=1, project=ROOT.name, data_kind='synthetic',
                  config=config, config_sha256=digest((ROOT/'config.json').read_bytes()),
                  source_sha256=digest(Path(__file__).read_bytes()),
                  data_sha256=digest(data), metrics=metrics)
    result_bytes = encode(result)
    report = ('# Verified synthetic experiment\n\n'
              'Educational engineering benchmark. No clinical validity is claimed.\n\n'
              'Generated from `config.json` by `pipeline.py`. Metrics are computed, never hand-entered.\n\n'
              '```json\n' + json.dumps(metrics, indent=2, sort_keys=True, allow_nan=False) + '\n```\n\n'
              'Result SHA-256: `' + digest(result_bytes) + '`\n').encode()
    return {'data.csv':data,'results.json':result_bytes,'report.md':report}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true',help='Recompute and compare every result byte; do not overwrite')
    parser.add_argument('--output',type=Path,default=ROOT/'results')
    args = parser.parse_args()
    files = experiment()
    manifest = {name:digest(data) for name,data in files.items()}
    files['manifest.json'] = encode(manifest)
    if args.verify:
        for name,data in files.items():
            path = args.output/name
            if not path.exists() or path.read_bytes() != data:
                raise SystemExit('Verification failed: '+name)
        print('Verified: deterministic recomputation and all artifact checksums match')
    else:
        args.output.mkdir(parents=True,exist_ok=True)
        for name,data in files.items():
            (args.output/name).write_bytes(data)
        print('Generated synthetic data, measured results, report and checksums')

if __name__ == '__main__':
    main()
