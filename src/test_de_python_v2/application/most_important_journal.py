import networkx as nwx
import operator



def get_most_important_journal(graph:nwx.MultiGraph):
    '''
    Get a most important journal from a graph. Note that if there is several journals, you will retrieve only one
    @parameter : graph
    @return : tuple
    '''
    edge_list = list(graph.edges(data=True))
    journal_edge = {}
    unique_journal = {}
    count_journal = {}


    for (source , target, dict) in edge_list:

        if 'journal' in dict.keys():
            if dict['journal'] not in journal_edge.keys():
                journal_edge[dict['journal']] = [source , target]
            else:
                journal_edge[dict['journal']].extend([source, target])


    for key in journal_edge:
        unique_journal[key] = set(journal_edge[key])


    for key in unique_journal:
        counter = 0
        for val in unique_journal[key]:
            if(val != ""):
                counter = counter + 1

        count_journal[key] = counter

    a_famous_journal = max(count_journal.items(), key=operator.itemgetter(1))

    return a_famous_journal