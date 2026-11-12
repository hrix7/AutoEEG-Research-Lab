import json
from pathlib import Path
import re
import unittest

class WorkflowPolicy(unittest.TestCase):
    def test_safe_daily_workflow(self):
        path=Path(__file__).resolve().parents[1]/'.github/workflows/daily.yml'
        workflow=json.loads(path.read_text())
        self.assertEqual(workflow['permissions'],{'contents':'read'})
        self.assertEqual(len(workflow['on']['schedule']),1)
        self.assertIn('pull_request',workflow['on'])
        self.assertNotIn('pull_request_target',workflow['on'])
        validate=workflow['jobs']['validate']
        publish=workflow['jobs']['publish']
        self.assertEqual(publish['needs'],'validate')
        self.assertEqual(publish['permissions'],{'contents':'write'})
        self.assertIn("github.event_name == 'schedule'",publish['if'])
        self.assertIn('github.event.repository.default_branch',publish['if'])
        self.assertFalse(validate['steps'][0]['with']['persist-credentials'])
        for job in workflow['jobs'].values():
            self.assertLessEqual(job['timeout-minutes'],10)
            for step in job['steps']:
                if 'uses' in step:
                    self.assertRegex(step['uses'],r'^actions/[a-z-]+@[0-9a-f]{40}$')
        publish_commands='\n'.join(s.get('run','') for s in publish['steps'])
        self.assertIn('pipeline.py --verify',publish_commands)
        self.assertIn('git add -- results/',publish_commands)
        self.assertNotIn('--force',publish_commands)
