import networkx as nx
import luigi
import pandas as pd
from test_de_python_v2.job.generate_graph import generate_graph
from test_de_python_v2.workflow.prepare_pubmed_worflow import PreparePubmed
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
import simplejson as json


class GenerateGraph(luigi.Task):
    '''
      Generate a luigi worflow that generate a graph and save the results
      Paarameters are in the config file
      '''

    output_drugs_file = luigi.Parameter()
    output_clinical_file = luigi.Parameter()
    output_pubmed_file = luigi.Parameter()
    output_graph_image = luigi.Parameter()
    output_graph_json = luigi.Parameter()

    def requires(self):
        return PreparePubmed()


    def output(self):
        return luigi.LocalTarget(self.output_graph_json)

    def run(self):

        with self.output().temporary_path() as output_path:
            drug_prepare = pd.read_csv(self.output_drugs_file).fillna('')
            pubmed_prepare = pd.read_csv(self.output_pubmed_file).fillna('')
            clinical_prepare = pd.read_csv(self.output_clinical_file).fillna('')

            graph = generate_graph(drug_prepare, pubmed_prepare, clinical_prepare)

            #we write result
            nx.draw(graph, with_labels=True)
            plt.savefig(self.output_graph_image)

            graph_json = json_graph.node_link_data(graph)

            with open(output_path, 'w') as outfile:
                json.dump(graph_json, outfile)


