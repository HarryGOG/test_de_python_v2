import networkx as nwx
from test_de_python_v2.common import network
import pandas as pd


def generate_graph(drug_prepare:pd.DataFrame, pubmed_prepare:pd.DataFrame, clinical_prepare:pd.DataFrame):
    '''
      Generate a graph using pubmed, drugs, clinical trials data
      @parameter : drug_prepare
      @parameter : pubmed_prepare
      @parameter : clinical_prepare
      @return : graph_with_clinical_journal (a graph)
      '''

    #initialize the graph
    graph = nwx.MultiGraph()

    #generate nodes as drugs and add in the graph
    drugs_list_graph = network.generate_nodes_drugs(drug_prepare)
    graph_with_nodes = network.add_drugs_in_graph(graph, drugs_list_graph)

    #generate edge from pudmed data and add it in the graph
    drugs_list = list(graph_with_nodes.nodes)
    pubmed_edge, pubmed_journal_edge = network.generate_pubmed_edge(pubmed_prepare, drugs_list)
    graph_with_pubmed = network.add_edge_pubmed_in_graph(graph_with_nodes, pubmed_edge)
    graph_with_pubmed_journal = network.add_edge_journal_in_graph(graph_with_pubmed, pubmed_journal_edge)


    #generate edge from clinical trial data and add it in the graph
    clinical_edge, clinical_journal_edge= network.generate_clinical_edge(clinical_prepare, drugs_list)
    graph_with_clinical = network.add_edge_clinical_in_graph(graph_with_pubmed_journal, clinical_edge)
    graph_with_clinical_journal = network.add_edge_journal_in_graph(graph_with_clinical, clinical_journal_edge)


    return graph_with_clinical_journal


