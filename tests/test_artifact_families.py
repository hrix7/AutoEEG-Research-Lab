import hashlib,json,math,unittest
import pipeline as p
class ArtifactFamilyTests(unittest.TestCase):
 def test_known_support_and_independent_formulas(self):
  for family in ('pulse','blink','muscle'):
   x=p.artifact_component(128,2,family,100)
   self.assertEqual(len(x),256);self.assertTrue(all(v==0 for v in x[:64]+x[96:]))
   for j in range(32):
    expected=100*(1 if family=='pulse' else math.sin(math.pi*j/32)**2 if family=='blink' else math.sin(2*math.pi*30*j/128)*math.sin(math.pi*j/32)**2)
    self.assertAlmostEqual(x[64+j],expected,places=12)
 def test_invalid_family_and_amplitude(self):
  for family,amplitude in [('unknown',1),('pulse',-1),('blink',float('nan')),('muscle',True)]:
   with self.assertRaises(ValueError):p.artifact_component(128,2,family,amplitude)
 def test_export_hash_and_rejection_recompute(self):
  c=json.loads((p.ROOT/'config.json').read_text());r=p.artifact_family_probe(c);self.assertEqual(len(r['cases']),9)
  for row in r['cases']:
   x=[c['alpha_uV']*math.sin(2*math.pi*10*i/c['fs_hz'])+4*math.sin(2*math.pi*20*i/c['fs_hz'])+v for i,v in enumerate(p.artifact_component(c['fs_hz'],c['seconds'],row['family'],row['injected_amplitude_uV']))]
   self.assertEqual(row['signal_sha256'],hashlib.sha256(p.encode(x)).hexdigest());self.assertEqual(row['rejected'],max(x)-min(x)>c['peak_to_peak_limit_uV'])
