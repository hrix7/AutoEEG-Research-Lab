import math,unittest
import pipeline as p
class WindowTests(unittest.TestCase):
 def test_hann_reduces_far_bin_leakage_off_bin(self):
  xs=[math.sin(2*math.pi*10.3*i/128) for i in range(256)]
  self.assertLess(p.spectral_power(xs,128,20,'hann'),p.spectral_power(xs,128,20)*.01)
 def test_hann_normalization_matches_independent_complex_sum(self):
  xs=[math.sin(2*math.pi*10*i/128) for i in range(256)]
  import cmath,statistics
  w=[math.sin(math.pi*i/255)**2 for i in range(256)]
  z=sum((x-statistics.mean(xs))*v*cmath.exp(-2j*math.pi*10*i/128) for i,(x,v) in enumerate(zip(xs,w)))
  self.assertAlmostEqual(p.spectral_power(xs,128,10,'hann'),2*abs(z)**2/(128*sum(v*v for v in w)))
 def test_flat_accepted_epoch_has_undefined_spectrum(self):
  c=dict(seed=1,fs_hz=128,seconds=2,alpha_uV=0,noise_levels=[0],epochs_per_noise=2,peak_to_peak_limit_uV=150)
  # Remove both sinusoids explicitly, keeping acceptance and accounting path real.
  from unittest.mock import patch
  with patch.object(p,'signal_epoch',return_value=[1]*256):
   _,result=p.run(c)
  row=result['conditions'][0];self.assertEqual(row['accepted'],2);self.assertEqual(row['spectral_epochs'],0);self.assertIsNone(row['mean_peak_hz']);self.assertIsNone(row['hann_mean_alpha_fraction'])
 def test_invalid_window_rejected(self):
  with self.assertRaises(ValueError):p.spectral_power([1,2,3],128,10,'unknown')
