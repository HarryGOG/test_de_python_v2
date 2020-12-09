from unittest import TestCase
from test_de_python_v2.job.generate_graph import generate_graph
from test_de_python_v2.job.prepare_drugs_data import prepare_drugs
from test_de_python_v2.job.prepare_pubmed_data import prepare_pubmed
from test_de_python_v2.job.prepare_clinical_trials_data import prepare_clinical
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from networkx.readwrite import json_graph
import simplejson as json

class GraphTest(TestCase):

    def test_generate_graph(self):
        pubmed_json = pd.read_json(r'tests/test_data/pubmed_fix.json').fillna('')
        pubmed_csv = pd.read_csv("tests/test_data/pubmed.csv").fillna('')
        pubmed_prepare = prepare_pubmed(pubmed_csv, pubmed_json)

        drug_prepare = prepare_drugs(pd.read_csv("tests/test_data/drugs.csv").fillna(''))
        clinical_prepare = prepare_clinical(pd.read_csv("tests/test_data/clinical_trials.csv").fillna(''))

        graph = generate_graph(drug_prepare, pubmed_prepare, clinical_prepare)

        print(graph.nodes(data=True))
        print(graph.edges(data=True))

        nodes = [('', {'atccode': ''}), ('isoprenaline', {'atccode': '6302001'}),
                 ('epinephrine', {'atccode': 'a01ad'}), ('atropine', {'atccode': 'a03ba'}),
                 ('diphenhydramine', {'atccode': 'a04ad'}), ('betamethasone', {'atccode': 'r01ad'}),
                 ('tetracycline', {'atccode': 's03aa'}), ('ethanol', {'atccode': 'v03ab'})]

        edges = [('', 'diphenhydramine', {'id_pubmed': 1, 'title_pubmed': 'a 44-year-old man with erythema of the face diphenhydramine, neck, and chest, weakness, and palpitations',
                                          'date': '01/01/2019'}),
                 ('', 'diphenhydramine', {'id_pubmed': 2, 'title_pubmed': 'an evaluation of benadryl, pyribenzamine, and other so-called diphenhydramine antihistaminic drugs in the treatment of allergy.',
                                          'date': '01/01/2019'}), ('', 'diphenhydramine', {'id_pubmed': 3, 'title_pubmed': 'diphenhydramine hydrochloride helps symptoms of ciguatera fish poisoning.',
                                                                                           'date': '02/01/2019'}),
                 ('', 'diphenhydramine', {'journal': 'journal of emergency nursing', 'date': '01/01/2019'}),
                 ('', 'diphenhydramine', {'journal': 'the journal of pediatrics', 'date': '02/01/2019'}),
                 ('', 'diphenhydramine', {'id_clinical': 'NCT01967433', 'title_clinical': 'use of diphenhydramine as an adjunctive sedative for colonoscopy in patients chronically on opioids',
                                          'date': '01/01/2020'}),
                 ('', 'diphenhydramine', {'id_clinical': 'NCT04189588', 'title_clinical': 'phase 2 study iv quzyttir (cetirizine hydrochloride injection) vs v diphenhydramine', 'date': '01/01/2020'}), ('', 'diphenhydramine', {'id_clinical': 'NCT04237091', 'title_clinical': 'feasibility of a randomized controlled clinical trial comparing the use of cetirizine to replace diphenhydramine in the prevention of reactions related to paclitaxel', 'date': '01/01/2020'}), ('', 'diphenhydramine', {'journal': 'journal of emergency nursing', 'date': '01/01/2020'}), ('', 'tetracycline', {'id_pubmed': 4, 'title_pubmed': 'tetracycline resistance patterns of lactobacillus buchneri group strains.', 'date': '01/01/2020'}), ('', 'tetracycline', {'id_pubmed': 5, 'title_pubmed': 'appositional tetracycline bone formation rates in the beagle.', 'date': '02/01/2020'}), ('', 'tetracycline', {'id_pubmed': 6, 'title_pubmed': 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.', 'date': '01/01/2020'}), ('', 'tetracycline', {'journal': 'journal of food protection', 'date': '01/01/2020'}), ('', 'tetracycline', {'journal': 'american journal of veterinary research', 'date': '02/01/2020'}), ('', 'tetracycline', {'journal': 'psychopharmacology', 'date': '01/01/2020'}), ('', 'ethanol', {'id_pubmed': 6, 'title_pubmed': 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.', 'date': '01/01/2020'}), ('', 'ethanol', {'journal': 'psychopharmacology', 'date': '01/01/2020'}), ('', 'epinephrine', {'id_pubmed': 7, 'title_pubmed': 'the high cost of epinephrine autoinjectors and possible alternatives.', 'date': '01/02/2020'}), ('', 'epinephrine', {'id_pubmed': 8, 'title_pubmed': 'time to epinephrine treatment is associated with the risk of mortality in children who achieve sustained rosc after traumatic out-of-hospital cardiac arrest.', 'date': '01/03/2020'}), ('', 'epinephrine', {'journal': 'the journal of allergy and clinical immunology. in practice', 'date': '01/02/2020'}), ('', 'epinephrine', {'journal': 'the journal of allergy and clinical immunology. in practice', 'date': '01/03/2020'}), ('', 'epinephrine', {'id_clinical': 'NCT04188184', 'title_clinical': 'tranexamic acid versus epinephrine during exploratory tympanotomy', 'date': '27/04/2020'}), ('', 'epinephrine', {'journal': 'journal of emergency nursing', 'date': '27/04/2020'}), ('', 'isoprenaline', {'id_pubmed': 9, 'title_pubmed': 'gold nanoparticles synthesized from euphorbia fischeriana root by green route method alleviates the isoprenaline hydrochloride induced myocardial infarction in rats.', 'date': '01/01/2020'}), ('', 'isoprenaline', {'journal': 'journal of photochemistry and photobiology. b, biology', 'date': '01/01/2020'}), ('', 'betamethasone', {'id_pubmed': 10, 'title_pubmed': 'clinical implications of umbilical artery doppler changes after betamethasone administration', 'date': '01/01/2020'}), ('', 'betamethasone', {'id_pubmed': 11, 'title_pubmed': 'effects of topical application of betamethasone on imiquimod-induced psoriasis-like skin inflammation in mice.', 'date': '01/01/2020'}), ('', 'betamethasone', {'id_pubmed': 13, 'title_pubmed': 'comparison of pressure betamethasone release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius atropine muscle.', 'date': '03/01/2020'}), ('', 'betamethasone', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '01/01/2020'}), ('', 'betamethasone', {'journal': 'journal of back and musculoskeletal rehabilitation', 'date': '01/01/2020'}), ('', 'betamethasone', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '03/01/2020'}), ('', 'betamethasone', {'id_clinical': 'NCT04153396', 'title_clinical': 'preemptive infiltration with betamethasone and ropivacaine for postoperative pain in laminoplasty or  laminectomy', 'date': '01/01/2020'}), ('', 'betamethasone', {'journal': 'hopitaux universitaires de geneve', 'date': '01/01/2020'}), ('', 'atropine', {'id_pubmed': 13, 'title_pubmed': 'comparison of pressure betamethasone release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius atropine muscle.', 'date': '03/01/2020'}), ('', 'atropine', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '03/01/2020'}), ('atropine', 'betamethasone', {'id_pubmed': 13, 'title_pubmed': 'comparison of pressure betamethasone release, phonophoresis and dry needling in treatment of latent myofascial trigger point of upper trapezius atropine muscle.', 'date': '03/01/2020'}), ('atropine', 'betamethasone', {'journal': 'the journal of maternal-fetal & neonatal medicine', 'date': '03/01/2020'}), ('tetracycline', 'ethanol', {'id_pubmed': 6, 'title_pubmed': 'rapid reacquisition of contextual fear following extinction in mice: effects of amount of extinction, tetracycline acute ethanol withdrawal, and ethanol intoxication.', 'date': '01/01/2020'}), ('tetracycline', 'ethanol', {'journal': 'psychopharmacology', 'date': '01/01/2020'})]

        self.assertListEqual(list(graph.nodes(data=True)), nodes)
        self.assertListEqual(list(graph.edges(data=True)), edges)


        nx.draw(graph, with_labels=True)
        plt.savefig("tests/test_data/drug_graph.png")

        graph_json = json_graph.node_link_data(graph)
        #print(graph_json)

        with open("tests/test_data/drug_graph.json", 'w') as outfile:
            json.dump(graph_json, outfile)

