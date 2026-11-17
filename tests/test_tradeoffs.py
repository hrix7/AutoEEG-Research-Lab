import unittest
import pipeline as p
class TradeoffTests(unittest.TestCase):
 def test_hand_counted_fixed_thresholds_and_strict_boundary(self):
  rows=p.rejection_tradeoffs([(50,False),(100,False),(200,True),(350,True)])
  self.assertEqual([(r['true_positives'],r['false_positives'],r['false_negatives'],r['true_negatives']) for r in rows],[(2,1,0,1),(2,0,0,2),(1,0,1,2)])
  self.assertEqual(p.rejection_tradeoffs([(150,True)],(150,))[0]['false_negatives'],1)
 def test_empty_detection_denominators_explicit(self):
  r=p.rejection_tradeoffs([(10,False)])[0];self.assertIsNone(r['precision']);self.assertIsNone(r['recall'])
