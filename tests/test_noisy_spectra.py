import json,math,random,unittest
from pathlib import Path
import pipeline as p
class NoisySpectrumTests(unittest.TestCase):
 def test_paired_clean_spectrum_matches_independent_dft(self):
  c=json.loads(Path('config.json').read_text());row=p.artifact_noise_probe(c)['cases'][0];fs=c['fs_hz'];rng=random.Random(row['seed'])
  x=[c['alpha_uV']*math.sin(2*math.pi*10*i/fs)+4*math.sin(2*math.pi*20*i/fs)+rng.gauss(0,row['noise_sd_uV']) for i in range(fs*c['seconds'])];offset=sum(x)/len(x)
  power={f:abs(sum((v-offset)*complex(math.cos(2*math.pi*f*i/fs),math.sin(2*math.pi*f*i/fs)) for i,v in enumerate(x)))**2 for f in range(1,41)}
  r=row['clean_diagnostic_spectra'][0];self.assertEqual(r['peak_hz'],max(power,key=power.get));self.assertAlmostEqual(r['alpha_fraction'],sum(power[f] for f in range(8,13))/sum(power.values()),places=12)
 def test_rejected_cases_keep_explicit_finite_diagnostics(self):
  c=json.loads(Path('config.json').read_text());c['noise_levels']=[0];rows=p.artifact_noise_probe(c)['cases']
  self.assertTrue(any(r['rejected'] for r in rows))
  for r in rows:
   self.assertEqual([v['window'] for v in r['diagnostic_spectra']],['rectangular','hann'])
   for v in r['diagnostic_spectra']:self.assertTrue(0<=v['alpha_fraction']<=1)
