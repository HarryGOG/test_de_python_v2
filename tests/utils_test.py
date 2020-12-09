from unittest import TestCase
from test_de_python_v2.common.utils import *
import pandas as pd


class CommonTest(TestCase):

    def test_normalize_string(self):
        string_with_accents = "éeuçàtest  BDO remove àéêöaccent Hôpitaux"

        result = normalize_string(string_with_accents)
        expected = "eeucatest  bdo remove aeeoaccent hopitaux"

        self.assertEqual(result, expected)


    def test_normalize_column(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv").fillna('')
        result = normalize_column(df, 'journal')

        expected = ["journal of emergency nursing", "journal of emergency nursing", "journal of emergency nursing",
                    "journal of emergency nursing" ,"hopitaux universitaires de geneve", "",
                    "journal of emergency nursing", "journal of emergency nursing"]

        self.assertListEqual(expected, result['journal'].tolist())


    def test_convert_to_date(self):
        date_string = '1 January 2020'
        result = convert_to_date(date_string, '%d %B %Y')
        expected = "01/01/2020"
        self.assertEqual(result, expected)

        date_string2 = '2020-01-01'
        result2 = convert_to_date(date_string2, '%Y-%m-%d')
        print(result2)
        expected2 = "01/01/2020"
        self.assertEqual(result2, expected2)


    def test_check_date(self):
        self.assertEqual(check_date("01/01/2020"), True)


    def test_prepare_date(self):

        result = prepare_date('1 January 2020', "/", '%d %B %Y')
        expected = "01/01/2020"
        self.assertEqual(result, expected)

        result2 = prepare_date('2020-01-01', "/", '%Y-%m-%d')
        expected2 = "01/01/2020"
        self.assertEqual(result2, expected2)


    def test_convert_column_date(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv").fillna('')

        result = convert_column_date(df, "/", '%d %B %Y')
        expected = ['01/01/2020', '01/01/2020', '01/01/2020', '01/01/2020',
                    '01/01/2020', '25/05/2020', '25/05/2020', '27/04/2020']

        self.assertEqual(result['date'].tolist(), expected)



    def test_convert_column_date_to_string(self):

        df = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')

        result = convert_column_date_to_string(df, 'date')
        expected = ['01/01/2020', '01/01/2020', '01/01/2020', '03/01/2020', '03/01/2020']

        self.assertListEqual(df['date'].tolist(), expected)










