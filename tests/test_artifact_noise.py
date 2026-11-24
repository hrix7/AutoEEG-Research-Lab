import json,math,random,unittest
from pathlib import Path
import pipeline as p
class ArtifactNoiseTests(unittest.TestCase):
 def test_independent_reconstruction_and_fixed_seed_domain(self):
  c=json.loads(Path('config.json').read_text());r=p.artifact_noise_probe(c)
  self.assertEqual(len(r['cases']),3*len(c['noise_levels'])*9)
  self.assertEqual({x['seed'] for x in r['cases']},set(range(c['seed']+5000,c['seed']+5003)))
  fs=c['fs_hz']
  for row in r['cases']:
   rng=random.Random(row['seed']);base=[c['alpha_uV']*math.sin(2*math.pi*10*i/fs)+4*math.sin(2*math.pi*20*i/fs)+rng.gauss(0,row['noise_sd_uV']) for i in range(fs*c['seconds'])]
   x=[a+b for a,b in zip(base,p.artifact_component(fs,c['seconds'],row['family'],row['amplitude_uV']))]
   self.assertEqual(row['signal_sha256'],p.digest(p.encode(x)))
   self.assertEqual(row['rejected'],max(x)-min(x)>c['peak_to_peak_limit_uV'])
   self.assertEqual(row['clean_rejected'],max(base)-min(base)>c['peak_to_peak_limit_uV'])
 def test_zero_noise_is_seed_invariant_and_rng_state_untouched(self):
  c=json.loads(Path('config.json').read_text());c['noise_levels']=[0]
  before=random.getstate();rows=p.artifact_noise_probe(c)['cases'];self.assertEqual(before,random.getstate())
  self.assertEqual([r['signal_sha256'] for r in rows[:9]],[r['signal_sha256'] for r in rows[9:18]])
