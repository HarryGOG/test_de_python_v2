from test_de_python_v2.application.most_important_journal import get_most_important_journal
from unittest import TestCase
import pandas as pd

from test_de_python_v2.job.generate_graph import generate_graph
from test_de_python_v2.job.prepare_clinical_trials_data import prepare_clinical
from test_de_python_v2.job.prepare_drugs_data import prepare_drugs
from test_de_python_v2.job.prepare_pubmed_data import prepare_pubmed


class MostImportJournalTest(TestCase):

    def test_get_most_important_journal(self):
        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        pubmed_prepare = prepare_pubmed(pubmed_csv, pubmed_json)

        drug_prepare = prepare_drugs(pd.read_csv("tests/test_data/drugs.csv").fillna(''))
        clinical_prepare = prepare_clinical(pd.read_csv("tests/test_data/clinical_trials.csv").fillna(''))

        graph = generate_graph(drug_prepare, pubmed_prepare, clinical_prepare)

        result = get_most_important_journal(graph)
        expected = ('journal of emergency nursing', 2)

        self.assertTupleEqual(result, expected)