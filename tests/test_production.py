import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('production',ROOT/'scripts/production.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class ProductionTests(unittest.TestCase):
    def setUp(self): self.data=json.loads((ROOT/'examples/merge-package.json').read_text(encoding='utf-8'))
    def test_realistic_plan_has_coverage(self): self.assertEqual(module.validate(self.data),[])
    def test_dependency_cycle_is_rejected(self):
        self.data['tasks'][0]['depends_on']=['T-PACK']
        self.assertTrue(any('cycle' in e for e in module.validate(self.data)))
    def test_unassigned_deliverable_is_rejected(self):
        self.data['tasks'].pop()
        self.assertTrue(any('no task' in e for e in module.validate(self.data)))
    def test_acceptance_cannot_be_self_reported_without_evidence(self):
        self.data['tasks'][0]['status']='accepted'
        self.assertTrue(any('review' in e for e in module.validate(self.data)))
    def test_change_propagates_without_mutating_baseline(self):
        before=copy.deepcopy(self.data)
        affected=module.impact(self.data,['D-ORDER'])['affected_task_ids']
        self.assertEqual(set(affected),{'T-RULE','T-ART','T-PACK'})
        self.assertEqual(self.data,before)
    def test_no_silent_replacement_of_package_output(self):
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'sow';module.render(self.data,out)
            with self.assertRaises(FileExistsError): module.render(self.data,out)
            result=json.loads((out/'package.json').read_text(encoding='utf-8'))
            self.assertTrue(all(t['status']=='planned' for t in result['tasks']))
    def test_dangling_inputs_are_rejected(self):
        self.data['tasks'][0]['deliverable_ids']=['D-NOT-REAL']
        self.assertTrue(any('dangling' in e for e in module.validate(self.data)))

if __name__=='__main__': unittest.main()
