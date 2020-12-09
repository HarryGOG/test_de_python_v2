from unittest import TestCase
from test_de_python_v2.common.fill_empty import *
import pandas as pd


class FillEmptyTest(TestCase):

    def test_find_similar_id(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv", dtype=str).fillna('')
        date="25/05/2020"
        scientific_title = "Glucagon Infusion in T1D Patients With Recurrent Severe Hypoglycemia: Effects on Counter-Regulatory Responses"

        result = find_similar_id(scientific_title, date, df)
        expected = "NCT03490942"

        self.assertEqual(result, expected)

    def test_fill_empty_id_method1(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv", dtype=str).fillna('')

        result = fill_empty_id_method1(df)

        expected = ['NCT01967433', 'NCT04189588', 'NCT04237090', 'NCT04237091',
                    'NCT04153396', 'NCT03490942', 'NCT03490942', 'NCT04188184']

        self.assertListEqual(expected, result['id'].tolist())


    def test_find_similar_journal(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv", dtype=str).fillna('')
        date = "25/05/2020"
        scientific_title = "Glucagon Infusion in T1D Patients With Recurrent Severe Hypoglycemia: Effects on Counter-Regulatory Responses"

        result = find_similar_journal(scientific_title, date, df)
        print(result)
        expected = "Journal of emergency nursing"

        self.assertEqual(result, expected)

    def test_fill_empty_journal(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv", dtype=str).fillna('')
        result = fill_empty_journal(df)

        expected = ['Journal of emergency nursing', 'Journal of emergency nursing', 'Journal of emergency nursing',
                    'Journal of emergency nursing', 'Hôpitaux Universitaires de Genève', 'Journal of emergency nursing',
                    'Journal of emergency nursing', 'Journal of emergency nursing\\xc3\\x28']

        self.assertListEqual(expected, result['journal'].tolist())


    def test_extract_int(self):
        result = extract_int("12")
        self.assertEqual(result, 12)


    def test_formated_id_column(self):
        df = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        result = formated_id_column(df)

        expected = [9, 10, 11, 12, 0]
        self.assertListEqual(result['id'].tolist(), expected)


    def test_formated_id_column(self):
        df = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        result = fill_empty_id_method2(df)

        expected = [9, 10, 11, 12, 13]
        self.assertListEqual(result['id'].tolist(), expected)
