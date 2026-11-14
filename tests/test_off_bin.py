import unittest,math
import pipeline as p
class OffBinProbeTests(unittest.TestCase):
 def test_fixed_grid_reports_nonzero_resolution_error(self):
  result=p.off_bin_probe(128,2)
  self.assertEqual(result['generator_frequency_hz'],10.3)
  for row in result['estimates']:
   self.assertEqual(row['peak_hz'],10);self.assertAlmostEqual(row['absolute_peak_error_hz'],.3)
   self.assertTrue(0<=row['far_grid_fraction']<=1)
  self.assertLess(result['estimates'][1]['far_grid_fraction'],result['estimates'][0]['far_grid_fraction'])
 def test_probe_reproducible_without_random_state(self):
  self.assertEqual(p.off_bin_probe(128,2),p.off_bin_probe(128,2))
  self.assertEqual(p.off_bin_probe(128,2,10)['estimates'][0]['absolute_peak_error_hz'],0)

 def test_invalid_probe_inputs_fail_explicitly(self):
  for args in [(128,2,0),(128,2,float('nan')),(128,0,10),(80,2,10)]:
   with self.assertRaises(ValueError):p.off_bin_probe(*args)
