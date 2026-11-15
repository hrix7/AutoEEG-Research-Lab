import unittest,json
import pipeline as p
class ConfigContractTests(unittest.TestCase):
 def test_invalid_config_rejected_before_generation(self):
  valid=json.loads((p.ROOT/'config.json').read_text())
  for key,value in [('fs_hz',40),('fs_hz',128.5),('seconds',0),('epochs_per_noise',0),('epochs_per_noise',True),('seed',True),('alpha_uV',float('nan')),('peak_to_peak_limit_uV',-1),('noise_levels',[]),('noise_levels',[1,1]),('noise_levels',[True]),('noise_levels',[float('inf')]),('noise_levels',[-1])]:
   c={**valid,key:value}
   with self.subTest(key=key,value=value):
    with self.assertRaises(ValueError):p.run(c)
 def test_zero_threshold_and_zero_noise_are_valid(self):
  c=json.loads((p.ROOT/'config.json').read_text());c.update(epochs_per_noise=1,noise_levels=[0],peak_to_peak_limit_uV=0)
  _,m=p.run(c);self.assertEqual(m['conditions'][0]['rejected'],1)
