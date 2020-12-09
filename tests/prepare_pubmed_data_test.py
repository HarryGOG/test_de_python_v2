from unittest import TestCase
import pandas as pd
from test_de_python_v2.job.prepare_pubmed_data import prepare_pubmed


class PubmedTest(TestCase):

    def test_prepare_pubmed(self):

        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        result = prepare_pubmed(pubmed_csv, pubmed_json)


        expected = { 'id' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                     'title':['a 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations', 'an evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.', 'diphenhydramine hydrochloride helps symptoms of ciguatera fish poisoning.', 'tetracycline resistance patterns of lactobacillus buchneri group strains.', 'appositional tetracycline bone formation rates in the beagle.', 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.', 'the high cost of epinephrine autoinjectors and possible alternatives.', 'time to epinephrine treatment is associated with the risk of mortality in children who achieve sustained rosc after traumatic out-of-hospital cardiac arrest.', 'gold nanoparticles synthesized from euphorbia fischeriana root by green route method alleviates the isoprenaline hydrochloride induced myocardial infarction in rats.', 'clinical implications of umbilical artery doppler changes after betamethasone administration', 'effects of topical application of betamethasone on imiquimod-induced psoriasis-like skin inflammation in mice.', 'comparison of pressure release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius muscle.', 'comparison of pressure betamethasone release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius atropine muscle.'],
                     'date': ['01/01/2019', '01/01/2019', '02/01/2019', '01/01/2020', '02/01/2020', '01/01/2020', '01/02/2020', '01/03/2020', '01/01/2020', '01/01/2020', '01/01/2020', '03/01/2020', '03/01/2020'],
                     'journal': ['journal of emergency nursing', 'journal of emergency nursing', 'the journal of pediatrics', 'journal of food protection', 'american journal of veterinary research', 'psychopharmacology', 'the journal of allergy and clinical immunology. in practice', 'the journal of allergy and clinical immunology. in practice', 'journal of photochemistry and photobiology. b, biology', 'the journal of maternal-fetal & neonatal medicine', 'journal of back and musculoskeletal rehabilitation', 'journal of back and musculoskeletal rehabilitation', 'the journal of maternal-fetal & neonatal medicine']
        }

        self.assertListEqual(result['id'].tolist(), expected['id'])
        self.assertListEqual(result['title'].tolist(), expected['title'])
        self.assertListEqual(result['date'].tolist(), expected['date'])
        self.assertListEqual(result['journal'].tolist(), expected['journal'])


