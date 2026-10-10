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
    def test_detailed_case_exports_and_traces_only_relevant_work(self):
        import csv
        case=json.loads((ROOT/'examples/community-order-detailed.json').read_text(encoding='utf-8'))
        self.assertEqual(module.validate(case),[])
        before=copy.deepcopy(case)
        self.assertEqual(module.impact(case,['D-CONFIG'])['affected_task_ids'],['T-02','T-07','T-08','T-10','T-11','T-12'])
        self.assertEqual(case,before)
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory)/'sow';module.render(case,out)
            for name,count in [('tasks.csv',12),('acceptance.csv',12),('asset-bom.csv',3)]:
                with (out/name).open(encoding='utf-8-sig') as f: self.assertEqual(len(list(csv.DictReader(f))),count)
            self.assertTrue(all(t['status']=='planned' for t in json.loads((out/'package.json').read_text(encoding='utf-8'))['tasks']))
    def test_pending_inputs_and_empty_acceptance_block_execution(self):
        case=json.loads((ROOT/'examples/community-order-detailed.json').read_text(encoding='utf-8'))
        case['tasks'][6]['status']='ready'
        self.assertTrue(any('pending inputs' in e for e in module.validate(case)))
        case['tasks'][6]['status']='planned'
        case['tasks'][6]['acceptance_cases'][0]['then']=''
        self.assertTrue(any('id/given/when/then' in e for e in module.validate(case)))
    def test_execution_cannot_skip_prerequisites_or_input_version_mapping(self):
        case=json.loads((ROOT/'examples/community-order-detailed.json').read_text(encoding='utf-8'))
        task=case['tasks'][6];task['status']='ready'
        for item in task['input_versions']: item['status']='available'
        self.assertTrue(any('prerequisite' in e for e in module.validate(case)))
        task['status']='planned';task['input_versions'][0]['ref']='D-NONEXISTENT'
        errors=module.validate(case)
        self.assertTrue(any('dangling versioned input' in e for e in errors))
        self.assertTrue(any('match inputs' in e for e in errors))
        duplicate=json.loads((ROOT/'examples/community-order-detailed.json').read_text(encoding='utf-8'))
        duplicate['tasks'][6]['inputs'].append('D-CONFIG')
        self.assertTrue(any('match inputs' in e for e in module.validate(duplicate)))
        for key in ['outputs','entry_criteria','stop_conditions']:
            altered=copy.deepcopy(case);altered['tasks'][6][key]=['  ']
            self.assertTrue(any(key+' needs nonblank' in e for e in module.validate(altered)))
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
