"""Test case for the worflow"""
import luigi
from unittest import TestCase
from test_de_python_v2.workflow import generate_graph_workflow, prepare_pubmed_worflow, prepare_drugs_workflow, prepare_clinical_worflow
from test_de_python_v2.common.workflow_utils import with_luigi_config
import os


@with_luigi_config("workflow-test.cfg")
class WorkflowLuigiTest(TestCase):

    def test_workflow(self):

        luigi.run(['--module', generate_graph_workflow.__name__,
                   'test_de_python_v2.workflow.generate_graph_workflow.GenerateGraph',
                   '--local-scheduler'])

        expected_path_drugs = "target/drugs_prepare.csv"
        expected_path_clinical = "target/clinical_trials_prepare.csv"
        expected_path_pubmeb = "target/pubmed_prepare.csv"
        expected_path_graph_image = "target/drugs_graph.png"
        expected_path_graph_json = "target/drugs_graph.json"

        # Use an assertion method to compare data frames
        self.assertEqual(True, os.path.exists(expected_path_drugs))
        self.assertEqual(True, os.path.exists(expected_path_clinical))
        self.assertEqual(True, os.path.exists(expected_path_pubmeb))
        self.assertEqual(True, os.path.exists(expected_path_graph_image))
        self.assertEqual(True, os.path.exists(expected_path_graph_json))


