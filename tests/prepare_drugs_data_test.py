from unittest import TestCase
from test_de_python_v2.job.prepare_drugs_data import prepare_drugs
import pandas as pd


class DrugTest(TestCase):

    def test_prepare_drugs(self):
        # pd.set_option('display.max_rows', None)
        # pd.set_option('display.max_columns', None)
        # pd.set_option('display.width', None)
        # pd.set_option('display.max_colwidth', -1)
        # print("\n")

        df = pd.read_csv("tests/test_data/drugs.csv").fillna('')
        result = prepare_drugs(df)

        expected = { 'atccode': ['6302001', 'a01ad', 'a03ba', 'a04ad', 'r01ad', 's03aa', 'v03ab'],
                     'drug':['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline', 'ethanol']
                     }

        self.assertListEqual(result['atccode'].tolist(), expected['atccode'])
        self.assertListEqual(result['drug'].tolist(), expected['drug'])


