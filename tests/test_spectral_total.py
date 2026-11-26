import unittest
from unittest.mock import patch
import pipeline as p
class SpectralTotalTests(unittest.TestCase):
 def test_finite_bins_with_overflowing_total_are_rejected(self):
  with patch.object(p,'spectral_power',return_value=1e307):
   with self.assertRaisesRegex(ValueError,'total spectral power'):p.diagnostic_spectra([0,1,0],128)
 def test_large_representable_total_preserves_fraction(self):
  with patch.object(p,'spectral_power',return_value=1e300):
   for r in p.diagnostic_spectra([0,1,0],128):self.assertAlmostEqual(r['alpha_fraction'],5/40)
