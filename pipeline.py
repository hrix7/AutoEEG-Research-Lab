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

def spectral_power(signal, fs, frequency):
    # One-sided periodogram at an integer DFT bin; units amplitude squared / Hz.
    n = len(signal)
    offset = mean(signal)
    centered = [x - offset for x in signal]
    re = sum(x * math.cos(2 * math.pi * frequency * i / fs) for i, x in enumerate(centered))
    im = sum(x * math.sin(2 * math.pi * frequency * i / fs) for i, x in enumerate(centered))
    return 2 * (re * re + im * im) / (fs * n)

def signal_epoch(rng, fs, seconds, alpha, noise, artifact):
    xs = [alpha * math.sin(2 * math.pi * 10 * i / fs)
          + 4 * math.sin(2 * math.pi * 20 * i / fs)
          + rng.gauss(0, noise) for i in range(fs * seconds)]
    if artifact:
        for i in range(fs // 2, fs // 2 + 8):
            xs[i] += 250
    return xs

def run(config):
    rng = random.Random(config['seed'])
    rows = [['epoch', 'noise_sd_uV', 'artifact_injected', 'sample', 'amplitude_uV']]
    results = []
    for noise in config['noise_levels']:
        accepted, peaks, ratios, rejected, tp = 0, [], [], 0, 0
        for epoch in range(config['epochs_per_noise']):
            artifact = epoch % 4 == 0
            xs = signal_epoch(rng, config['fs_hz'], config['seconds'], config['alpha_uV'], noise, artifact)
            rows.extend([epoch, noise, int(artifact), i, format(x, '.12g')] for i, x in enumerate(xs))
            reject = max(xs) - min(xs) > config['peak_to_peak_limit_uV']
            rejected += reject
            tp += reject and artifact
            if not reject:
                powers = {f: spectral_power(xs, config['fs_hz'], f) for f in range(1, 41)}
                peaks.append(max(powers, key=powers.get))
                ratios.append(sum(p for f, p in powers.items() if 8 <= f <= 12) / sum(powers.values()))
                accepted += 1
        results.append(dict(noise_sd_uV=noise, accepted=accepted, rejected=rejected,
                            artifact_true_positives=tp, artifact_injected=config['epochs_per_noise']//4,
                            mean_peak_hz=mean(peaks), mean_alpha_fraction=mean(ratios)))
    return rows, {'conditions': results, 'interpretation': 'Spectral recovery on generated sinusoids only; no disease labels or patient data.'}

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
