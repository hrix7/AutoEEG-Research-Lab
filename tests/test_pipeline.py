import copy
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import tempfile
import unittest
import pipeline as p

class Reproducibility(unittest.TestCase):
    def test_repeatable(self):
        self.assertEqual(p.experiment(), p.experiment())
    def test_all_metrics_finite(self):
        result = json.loads(p.experiment()['results.json'])
        def walk(x):
            if isinstance(x, float): self.assertTrue(math.isfinite(x))
            elif isinstance(x,dict):
                for v in x.values(): walk(v)
            elif isinstance(x,list):
                for v in x: walk(v)
        walk(result)
    def test_verifier_rejects_tampering(self):
        with tempfile.TemporaryDirectory() as d:
            cmd=[sys.executable,str(p.ROOT/'pipeline.py'),'--output',d]
            subprocess.run(cmd,check=True,capture_output=True)
            subprocess.run(cmd+['--verify'],check=True,capture_output=True)
            path=Path(d)/'data.csv'
            path.write_text('tampered')
            self.assertNotEqual(subprocess.run(cmd+['--verify'],capture_output=True).returncode,0)

class SignalTests(unittest.TestCase):
    def test_known_sine_power(self):
        xs=[3*math.sin(2*math.pi*10*i/128) for i in range(256)]
        self.assertAlmostEqual(p.spectral_power(xs,128,10),9,places=9)
        self.assertAlmostEqual(p.spectral_power(xs,128,20),0,places=9)
    def test_artifacts_and_peak(self):
        cfg=json.loads((p.ROOT/'config.json').read_text())
        rows,result=p.run(cfg)
        for condition in result['conditions']:
            self.assertEqual(condition['artifact_true_positives'],4)
            self.assertEqual(condition['accepted']+condition['rejected'],16)
            self.assertEqual(condition['mean_peak_hz'],10)
            self.assertTrue(0 <= condition['mean_alpha_fraction'] <= 1)

class ArtifactAccountingTests(unittest.TestCase):
    def config(self, **changes):
        cfg=json.loads((p.ROOT/'config.json').read_text())
        cfg.update(noise_levels=[2], **changes)
        return cfg

    def test_nonmultiple_epoch_count_matches_generated_labels(self):
        for count in (1, 3, 5, 7):
            with self.subTest(epochs=count):
                rows,result=p.run(self.config(epochs_per_noise=count))
                injected_epochs={r[0] for r in rows[1:] if r[2] == 1}
                condition=result['conditions'][0]
                self.assertEqual(condition['artifact_injected'], len(injected_epochs))
                self.assertEqual(condition['artifact_injected'], 1 if count <= 4 else 2)
                self.assertEqual(condition['artifact_false_positives'],0)
                self.assertEqual(condition['artifact_false_negatives'],0)

    def test_all_rejected_is_explicit_missing_spectral_result(self):
        rows,result=p.run(self.config(epochs_per_noise=4, peak_to_peak_limit_uV=.01))
        c=result['conditions'][0]
        self.assertEqual((c['accepted'],c['rejected']),(0,4))
        self.assertEqual((c['artifact_true_positives'],c['artifact_false_positives']),(1,3))
        self.assertEqual((c['artifact_true_negatives'],c['artifact_false_negatives']),(0,0))
        self.assertIsNone(c['mean_peak_hz'])
        self.assertIsNone(c['mean_alpha_fraction'])
        json.dumps(result, allow_nan=False)

    def test_all_accepted_records_missed_artifacts(self):
        rows,result=p.run(self.config(epochs_per_noise=5, peak_to_peak_limit_uV=10000))
        c=result['conditions'][0]
        self.assertEqual(c['accepted'],5)
        self.assertEqual(c['artifact_false_negatives'],2)
        self.assertEqual(c['artifact_true_negatives'],3)
        self.assertEqual(c['artifact_false_positives'],0)
