from test_de_python_v2.common.network import *
from test_de_python_v2.job.prepare_drugs_data import prepare_drugs
from test_de_python_v2.job.prepare_pubmed_data import prepare_pubmed
from test_de_python_v2.job.prepare_clinical_trials_data import prepare_clinical
from unittest import TestCase
import pandas as pd
import networkx as nwx


class NetworkTest(TestCase):

    def test_generate_nodes_drugs(self):
        data = pd.read_csv("tests/test_data/drugs.csv").fillna('')
        data_prepare = prepare_drugs(data)

        result = generate_nodes_drugs(data_prepare)
        #print(result)
        expected = [{'atccode': '', 'drug': ''}, {'atccode': '6302001', 'drug': 'isoprenaline'}, {'atccode': 'a01ad', 'drug': 'epinephrine'}, {'atccode': 'a03ba', 'drug': 'atropine'}, {'atccode': 'a04ad', 'drug': 'diphenhydramine'}, {'atccode': 'r01ad', 'drug': 'betamethasone'}, {'atccode': 's03aa', 'drug': 'tetracycline'}, {'atccode': 'v03ab', 'drug': 'ethanol'}]

        self.assertListEqual(result, expected)


    def test_add_drugs_in_graph(self):
        drugs_list = [{'atccode': '6302001', 'drug': 'isoprenaline'}, {'atccode': 'a01ad', 'drug': 'epinephrine'},
         {'atccode': 'a03ba', 'drug': 'atropine'}, {'atccode': 'a04ad', 'drug': 'diphenhydramine'},
         {'atccode': 'r01ad', 'drug': 'betamethasone'}, {'atccode': 's03aa', 'drug': 'tetracycline'},
         {'atccode': 'v03ab', 'drug': 'ethanol'}]

        graph = nwx.MultiGraph()
        result = add_drugs_in_graph(graph, drugs_list)

        expected = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline', 'ethanol']

        self.assertListEqual(list(result.nodes), expected)


    def test_extract_drugs_from_title(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline', 'ethanol']
        title = "Feasibility betamethasone a Randomized Controlled Clinical atropine Trial Comparing the Use of Cetirizine to Replace diphenhydramine in the Prevention of Reactions Related to Paclitaxel"

        result = extract_drugs_from_title(drugs_list, title)
        expected = ['atropine', 'diphenhydramine', 'betamethasone']

        self.assertListEqual(result, expected)


    def test_generate_drugs_edge(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']

        result = generate_drugs_edge(drugs_list)
        expected = [('isoprenaline', 'epinephrine'), ('isoprenaline', 'atropine'), ('isoprenaline', 'diphenhydramine'), ('isoprenaline', 'betamethasone'), ('isoprenaline', 'tetracycline'), ('isoprenaline', 'ethanol'), ('epinephrine', 'atropine'), ('epinephrine', 'diphenhydramine'), ('epinephrine', 'betamethasone'), ('epinephrine', 'tetracycline'), ('epinephrine', 'ethanol'), ('atropine', 'diphenhydramine'), ('atropine', 'betamethasone'), ('atropine', 'tetracycline'), ('atropine', 'ethanol'), ('diphenhydramine', 'betamethasone'), ('diphenhydramine', 'tetracycline'), ('diphenhydramine', 'ethanol'), ('betamethasone', 'tetracycline'), ('betamethasone', 'ethanol'), ('tetracycline', 'ethanol')]

        self.assertListEqual(result, expected)


    def test_generate_pubmed_edge(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']
        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        df = prepare_pubmed(pubmed_csv, pubmed_json)
        df = df[df.id==6]

        result_pubmed_edge, result_journal_edge = generate_pubmed_edge(df, drugs_list)
        #print(result_pubmed_edge)
        #print(result_journal_edge)

        expected_pubmed_edge = [{'id_pubmed': 6, 'title_pubmed': 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.', 'date': '01/01/2020', 'edge_list': [('tetracycline', 'ethanol')]}]
        expected_journal_edge = [{'journal': 'psychopharmacology', 'date': '01/01/2020', 'edge_list': [('tetracycline', 'ethanol')]}]

        self.assertListEqual(result_pubmed_edge, expected_pubmed_edge)
        self.assertListEqual(result_journal_edge, expected_journal_edge)


    def test_generate_clinical_edge(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']
        df = pd.read_csv("tests/test_data/clinical_trials.csv").fillna('')

        df = prepare_clinical(df)
        df = df[df.id == 'NCT01967433']

        result_clinical_edge, result_journal_edge = generate_clinical_edge(df, drugs_list)
        #print(result_clinical_edge)
        #print(result_journal_edge)

        expected_clinical_edge = [{'id_clinical': 'NCT01967433', 'title_clinical': 'use of diphenhydramine as an adjunctive sedative for colonoscopy in patients chronically on opioids', 'date': '01/01/2020', 'edge_list': [('diphenhydramine', '')]}]
        expected_journal_edge = [{'journal': 'journal of emergency nursing', 'date': '01/01/2020', 'edge_list': [('diphenhydramine', '')]}]

        self.assertListEqual(result_clinical_edge, expected_clinical_edge)
        self.assertListEqual(result_journal_edge, expected_journal_edge)


    def test_add_edge_pubmed_in_graph(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']

        drugs_list_graph = [{'atccode': '6302001', 'drug': 'isoprenaline'}, {'atccode': 'a01ad', 'drug': 'epinephrine'},
                      {'atccode': 'a03ba', 'drug': 'atropine'}, {'atccode': 'a04ad', 'drug': 'diphenhydramine'},
                      {'atccode': 'r01ad', 'drug': 'betamethasone'}, {'atccode': 's03aa', 'drug': 'tetracycline'},
                      {'atccode': 'v03ab', 'drug': 'ethanol'}]

        graph = nwx.MultiGraph()
        graph = add_drugs_in_graph(graph, drugs_list_graph)

        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        df = prepare_pubmed(pubmed_csv, pubmed_json)

        pubmed_edge, journal_edge = generate_pubmed_edge(df, drugs_list)
        graph_with_edge = add_edge_pubmed_in_graph(graph, pubmed_edge)


        expected = [('isoprenaline', '', {'id_pubmed': 9, 'title_pubmed': 'gold nanoparticles synthesized from euphorbia fischeriana root by green route method alleviates the isoprenaline hydrochloride induced myocardial infarction in rats.',
                                          'date': '01/01/2020'}),
                    ('epinephrine', '', {'id_pubmed': 7, 'title_pubmed': 'the high cost of epinephrine autoinjectors and possible alternatives.',
                                         'date': '01/02/2020'}),
                    ('epinephrine', '', {'id_pubmed': 8, 'title_pubmed': 'time to epinephrine treatment is associated with the risk of mortality in children who achieve sustained rosc after traumatic out-of-hospital cardiac arrest.',
                                         'date': '01/03/2020'}),
                    ('atropine', 'betamethasone', {'id_pubmed': 13, 'title_pubmed': 'comparison of pressure betamethasone release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius atropine muscle.',
                                                   'date': '03/01/2020'}),
                    ('diphenhydramine', '', {'id_pubmed': 1, 'title_pubmed': 'a 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations',
                                             'date': '01/01/2019'}),
                    ('diphenhydramine', '', {'id_pubmed': 2, 'title_pubmed': 'an evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.',
                                             'date': '01/01/2019'}),
                    ('diphenhydramine', '', {'id_pubmed': 3, 'title_pubmed': 'diphenhydramine hydrochloride helps symptoms of ciguatera fish poisoning.',
                                             'date': '02/01/2019'}),
                    ('betamethasone', '', {'id_pubmed': 10, 'title_pubmed': 'clinical implications of umbilical artery doppler changes after betamethasone administration',
                                           'date': '01/01/2020'}),
                    ('betamethasone', '', {'id_pubmed': 11, 'title_pubmed': 'effects of topical application of betamethasone on imiquimod-induced psoriasis-like skin inflammation in mice.',
                                           'date': '01/01/2020'}),
                    ('tetracycline', '', {'id_pubmed': 4, 'title_pubmed': 'tetracycline resistance patterns of lactobacillus buchneri group strains.',
                                          'date': '01/01/2020'}),
                    ('tetracycline', '', {'id_pubmed': 5, 'title_pubmed': 'appositional tetracycline bone formation rates in the beagle.',
                                          'date': '02/01/2020'}),
                    ('tetracycline', 'ethanol', {'id_pubmed': 6, 'title_pubmed': 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.',
                                                 'date': '01/01/2020'})]


        #print(graph_with_edge.edges(data=True))
        self.assertListEqual(list(graph_with_edge.edges(data=True)), expected)


    def test_add_edge_clinical_in_graph(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']

        drugs_list_graph = [{'atccode': '6302001', 'drug': 'isoprenaline'}, {'atccode': 'a01ad', 'drug': 'epinephrine'},
                            {'atccode': 'a03ba', 'drug': 'atropine'}, {'atccode': 'a04ad', 'drug': 'diphenhydramine'},
                            {'atccode': 'r01ad', 'drug': 'betamethasone'}, {'atccode': 's03aa', 'drug': 'tetracycline'},
                            {'atccode': 'v03ab', 'drug': 'ethanol'}]

        graph = nwx.MultiGraph()
        graph = add_drugs_in_graph(graph, drugs_list_graph)

        df = pd.read_csv("tests/test_data/clinical_trials.csv").fillna('')
        df = prepare_clinical(df)

        clinical_edge, journal_edge = generate_clinical_edge(df, drugs_list)
        graph_with_edge = add_edge_clinical_in_graph(graph, clinical_edge)

        print(graph_with_edge.edges(data=True))

        expected = [('epinephrine', '', {'id_clinical': 'NCT04188184', 'title_clinical': 'tranexamic acid versus epinephrine during exploratory tympanotomy',
                                         'date': '27/04/2020'}),
                    ('diphenhydramine', '', {'id_clinical': 'NCT01967433', 'title_clinical': 'use of diphenhydramine as an adjunctive sedative for colonoscopy in patients chronically on opioids',
                                             'date': '01/01/2020'}),
                    ('diphenhydramine', '', {'id_clinical': 'NCT04189588', 'title_clinical': 'phase 2 study iv quzyttir (cetirizine hydrochloride injection) vs v diphenhydramine',
                                             'date': '01/01/2020'}),
                    ('diphenhydramine', '', {'id_clinical': 'NCT04237091', 'title_clinical': 'feasibility of a randomized controlled clinical trial comparing the use of cetirizine to replace diphenhydramine in the prevention of reactions related to paclitaxel',
                                             'date': '01/01/2020'}),
                    ('betamethasone', '', {'id_clinical': 'NCT04153396', 'title_clinical': 'preemptive infiltration with betamethasone and ropivacaine for postoperative pain in laminoplasty or  laminectomy',
                                           'date': '01/01/2020'})]


        self.assertListEqual(list(graph_with_edge.edges(data=True)), expected)


    def test_add_edge_journal_in_graph(self):
        drugs_list = ['isoprenaline', 'epinephrine', 'atropine', 'diphenhydramine', 'betamethasone', 'tetracycline',
                      'ethanol']

        drugs_list_graph = [{'atccode': '6302001', 'drug': 'isoprenaline'}, {'atccode': 'a01ad', 'drug': 'epinephrine'},
                      {'atccode': 'a03ba', 'drug': 'atropine'}, {'atccode': 'a04ad', 'drug': 'diphenhydramine'},
                      {'atccode': 'r01ad', 'drug': 'betamethasone'}, {'atccode': 's03aa', 'drug': 'tetracycline'},
                      {'atccode': 'v03ab', 'drug': 'ethanol'}]

        graph = nwx.MultiGraph()
        graph = add_drugs_in_graph(graph, drugs_list_graph)

        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        df = prepare_pubmed(pubmed_csv, pubmed_json)

        pubmed_edge, journal_edge = generate_pubmed_edge(df, drugs_list)
        graph_with_edge = add_edge_journal_in_graph(graph, journal_edge)


        expected = [('isoprenaline', '', {'journal': 'journal of photochemistry and photobiology. b, biology', 'date': '01/01/2020'}),
             ('epinephrine', '', {'journal': 'the journal of allergy and clinical immunology. in practice', 'date': '01/02/2020'}),
             ('epinephrine', '', {'journal': 'the journal of allergy and clinical immunology. in practice', 'date': '01/03/2020'}),
             ('atropine', 'betamethasone', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '03/01/2020'}),
             ('diphenhydramine', '', {'journal': 'journal of emergency nursing', 'date': '01/01/2019'}),
             ('diphenhydramine', '', {'journal': 'the journal of pediatrics', 'date': '02/01/2019'}),
             ('betamethasone', '', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '01/01/2020'}),
             ('betamethasone', '', {'journal': 'journal of back and musculoskeletal rehabilitation', 'date': '01/01/2020'}),
             ('tetracycline', '', {'journal': 'journal of food protection', 'date': '01/01/2020'}),
             ('tetracycline', '', {'journal': 'american journal of veterinary research', 'date': '02/01/2020'}),
             ('tetracycline', 'ethanol', {'journal': 'psychopharmacology', 'date': '01/01/2020'})]


        #print(graph_with_edge.edges(data=True))
        self.assertListEqual(list(graph_with_edge.edges(data=True)), expected)



    def test_remove_duplicate_edge(self):
        test_list = [1, 3, 5, 6, 3, 5, 6, 1]

        result = remove_duplicate_edge(test_list)
        expected = [1, 3, 5, 6]

        self.assertListEqual(result, expected)



