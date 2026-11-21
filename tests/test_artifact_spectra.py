import math,unittest
import pipeline as p
class ArtifactSpectrumTests(unittest.TestCase):
 def test_clean_known_frequency_and_flat_undefined(self):
  x=[math.sin(2*math.pi*10*i/128) for i in range(256)]
  for r in p.diagnostic_spectra(x,128):
   self.assertEqual(r['peak_hz'],10);self.assertGreater(r['alpha_fraction'],.99)
  for r in p.diagnostic_spectra([1.]*256,128):
   self.assertIsNone(r['peak_hz']);self.assertIsNone(r['alpha_fraction'])
 def test_rectangular_summary_matches_independent_complex_dft(self):
  x=[math.sin(2*math.pi*10*i/128)+.5*math.sin(2*math.pi*30*i/128) for i in range(256)]
  powers={f:abs(sum(v*complex(math.cos(-2*math.pi*f*i/128),math.sin(-2*math.pi*f*i/128)) for i,v in enumerate(x)))**2 for f in range(1,41)}
  r=p.diagnostic_spectra(x,128)[0]
  self.assertEqual(r['peak_hz'],max(powers,key=powers.get));self.assertAlmostEqual(r['alpha_fraction'],sum(powers[f] for f in range(8,13))/sum(powers.values()),places=12)

 def test_unrepresentable_power_is_rejected_not_reported_as_infinity(self):
  x=[1e200*math.sin(2*math.pi*10*i/128) for i in range(256)]
  for window in ('rectangular','hann'):
   with self.assertRaisesRegex(ValueError,'finite numerical range'):p.spectral_power(x,128,10,window)
  with self.assertRaises(ValueError):p.diagnostic_spectra(x,128)
