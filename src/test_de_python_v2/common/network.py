import pandas as pd
import networkx as nwx


def generate_nodes_drugs(df:pd.DataFrame):
    '''
     Generate graph node as Drugs
     @parameter : df
     @return : drugs_list_graph
     '''
    drugs_list_graph = []

    #add an empty node
    drugs_list_graph.append({"atccode": "", "drug": ""})

    for index, row in df.iterrows():
        drugs_list_graph.append({"atccode":row["atccode"],"drug":row["drug"]})


    return drugs_list_graph


def add_drugs_in_graph(graph:nwx.MultiGraph, drugs_list_graph:list):
    '''
     Add graph node in a graph
     @parameter : graph
     @parameter :  drugs_list_graph
     @return : drugs_list_graph
     '''
    for item in drugs_list_graph:
        graph.add_node(item["drug"], atccode=item["atccode"])

    return graph


def extract_drugs_from_title(drugs_list:list, title:str):
    '''
     Retrieve the list of drugs that appear in the title
     @parameter : drugs_list
     @parameter :  title
     @return : drugs_in_title_list
     '''
    drugs_in_title_list = [drug for drug in drugs_list if drug in title]

    return drugs_in_title_list


def generate_drugs_edge(drugs_list):
    '''
     Generate a list of edge graph from list
     @parameter : drugs_list
     @parameter :  title
     @return : drugs_in_title_list
     '''
    drugs_edge = [(a, b) for a in drugs_list
                    for b in drugs_list if a != b]

    # we remove edge that already appear
    for a, b in drugs_edge:
        if (b, a) in drugs_edge:
            drugs_edge.remove((b,a))

    #If the drugs_list contain only one element, we need to keep this information
    if(len(drugs_list)==1) :
        if (drugs_list[0] != ''):
            drugs_edge.append((drugs_list[0], ""))

    return drugs_edge


def generate_pubmed_edge(df:pd.DataFrame, drugs_list:list):
    '''
     Generate a list of pubmed edge graph and journal edge graph from dataframe
     @parameter : df
     @parameter :  drugs_list
     @return : pubmed_edge_distinct, journal_edge_distinct
     '''
    pubmed_edge = []
    journal_edge = []

    for index, row in df.iterrows():
        drugs_in_title_list = extract_drugs_from_title(drugs_list, row["title"])
        edge_list = generate_drugs_edge(drugs_in_title_list)
        pubmed_edge.append({"id_pubmed":row["id"],  "title_pubmed":row["title"],
                            "date":row["date"], "edge_list":edge_list})

        journal_edge.append({"journal": row["journal"], "date":row["date"],
                             "edge_list": edge_list})


    #remove duplicate
    pubmed_edge_distinct = remove_duplicate_edge(pubmed_edge)
    journal_edge_distinct = remove_duplicate_edge(journal_edge)

    return pubmed_edge_distinct, journal_edge_distinct


def remove_duplicate_edge(edge_list:list):
    '''
      Remove duplicate edge
      @parameter : edge_list
      @return : pubmed_edge_distinct, journal_edge_distinct
      '''
    res = []
    [res.append(x) for x in edge_list if x not in res]

    return res


def generate_clinical_edge(df:pd.DataFrame, drugs_list):
    clinical_edge = []
    journal_edge = []

    for index, row in df.iterrows():
        drugs_in_title_list = extract_drugs_from_title(drugs_list, row["scientific_title"])
        edge_list = generate_drugs_edge(drugs_in_title_list)
        clinical_edge.append({"id_clinical":row["id"],  "title_clinical":row["scientific_title"],
                            "date":row["date"], "edge_list":edge_list})

        journal_edge.append({"journal": row["journal"], "date":row["date"],
                             "edge_list": edge_list})

    # remove duplicate
    clinical_edge_distinct = remove_duplicate_edge(clinical_edge)
    journal_edge_distinct = remove_duplicate_edge(journal_edge)

    return clinical_edge_distinct, journal_edge_distinct



def add_edge_pubmed_in_graph(graph:nwx.MultiGraph, pubmed_edge):

    for item in pubmed_edge:
        if item['edge_list']:
            for edge in item['edge_list']:
                graph.add_edge(edge[0], edge[1], id_pubmed=item['id_pubmed'],
                               title_pubmed=item['title_pubmed'], date=item['date'])

    return graph



def add_edge_clinical_in_graph(graph:nwx.MultiGraph, clinical_edge):

    for item in clinical_edge:
        if item['edge_list']:
            for edge in item['edge_list']:
                graph.add_edge(edge[0], edge[1], id_clinical=item['id_clinical'],
                               title_clinical=item['title_clinical'], date=item['date'])

    return graph


def add_edge_journal_in_graph(graph:nwx.MultiGraph, journal_edge):

    for item in journal_edge:
        if item['edge_list']:
            for edge in item['edge_list']:
                graph.add_edge(edge[0], edge[1], journal=item['journal'], date=item['date'])

    return graph


