from unittest import TestCase
from test_de_python_v2.job.prepare_clinical_trials_data import prepare_clinical
import pandas as pd


class ClinicalTrialTest(TestCase):

    def test_prepare_clinical(self):
        df = pd.read_csv("tests/test_data/clinical_trials.csv").fillna('')

        prepare_clinical(df)

        expected = {'id': ['NCT01967433', 'NCT04189588', 'NCT04237090', 'NCT04237091', 'NCT04153396', 'NCT03490942', 'NCT03490942','NCT04188184'],
        'scientific_title': ['use of diphenhydramine as an adjunctive sedative for colonoscopy in patients chronically on opioids',
                             'phase 2 study iv quzyttir (cetirizine hydrochloride injection) vs v diphenhydramine', '',
                             'feasibility of a randomized controlled clinical trial comparing the use of cetirizine to replace diphenhydramine in the prevention of reactions related to paclitaxel',
                             'preemptive infiltration with betamethasone and ropivacaine for postoperative pain in laminoplasty or  laminectomy',
                             'glucagon infusion in t1d patients with recurrent severe hypoglycemia: effects on counter-regulatory responses',
                             'glucagon infusion in t1d patients with recurrent severe hypoglycemia: effects on counter-regulatory responses',
                             'tranexamic acid versus epinephrine during exploratory tympanotomy'],
        'date': ['01/01/2020', '01/01/2020', '01/01/2020', '01/01/2020', '01/01/2020', '25/05/2020', '25/05/2020', '27/04/2020'],
        'journal': ['journal of emergency nursing', 'journal of emergency nursing', 'journal of emergency nursing', 'journal of emergency nursing', 'hopitaux universitaires de geneve', 'journal of emergency nursing', 'journal of emergency nursing', 'journal of emergency nursing']}

        self.assertListEqual(df['id'].tolist(), expected['id'])
        self.assertListEqual(df['scientific_title'].tolist(), expected['scientific_title'])
        self.assertListEqual(df['date'].tolist(), expected['date'])
        self.assertListEqual(df['journal'].tolist(), expected['journal'])
