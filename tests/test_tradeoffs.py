import unittest
import pipeline as p
class TradeoffTests(unittest.TestCase):
 def test_hand_counted_fixed_thresholds_and_strict_boundary(self):
  rows=p.rejection_tradeoffs([(50,False),(100,False),(200,True),(350,True)])
  self.assertEqual([(r['true_positives'],r['false_positives'],r['false_negatives'],r['true_negatives']) for r in rows],[(2,1,0,1),(2,0,0,2),(1,0,1,2)])
  self.assertEqual(p.rejection_tradeoffs([(150,True)],(150,))[0]['false_negatives'],1)
 def test_empty_detection_denominators_explicit(self):
  r=p.rejection_tradeoffs([(10,False)])[0];self.assertIsNone(r['precision']);self.assertIsNone(r['recall'])

 def test_invalid_measurements_labels_and_thresholds_rejected(self):
  for records in [[(float('nan'),False)],[(float('inf'),True)],[(-1,True)],[(10,1)],[(True,True)],[(10,)],iter([(10,True)])]:
   with self.subTest(records=str(records)):
    with self.assertRaises(ValueError):p.rejection_tradeoffs(records)
  for thresholds in [(),(1,1),(-1,),(float('nan'),),(True,),iter([1])]:
   with self.assertRaises(ValueError):p.rejection_tradeoffs([],thresholds)
 def test_zero_threshold_empty_records_and_nonmutation(self):
  records=[(0,True),(1,False)];before=list(records);r=p.rejection_tradeoffs(records,(0,))[0]
  self.assertEqual((r['true_positives'],r['false_positives'],r['false_negatives']),(0,1,1));self.assertEqual(records,before)
  r=p.rejection_tradeoffs([], (0,))[0];self.assertIsNone(r['precision']);self.assertIsNone(r['recall']);self.assertEqual(r['true_negatives'],0)
