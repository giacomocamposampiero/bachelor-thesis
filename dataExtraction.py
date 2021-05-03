# import mean and std deviation from numpy
from numpy import mean
from numpy import std
# import graph utility library
import networkx as nx
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join
# improt regex lib
import re
# import csv lib
import csv
# import experiment params
import params as pa
# cartesian product function
from itertools import product

def analyze_graph(graph):
    """
    Compute information about the networkx graph passed as argument
    
    Params
    ------
    graph : graph
            networkx graph which has to be analyzed
    Returns
    -------
    l : list
        list of metrics about the graph computed using networkx methods; the 
        list contains (read the lines as [position] [metric]:
            0 number_of_edges
            1 number_of_connected_components
            2 mean_clustering_index
            3 std_deviation_clustering_index
    """
    info = list()
    info.append(nx.number_of_edges(graph))
    info.append(nx.number_connected_components(graph))
    clustering = nx.clustering(graph)
    info.append(mean(list(clustering.values())))
    info.append(std(list(clustering.values())))
    return info
    
def graph_parameters(classes):
    """
    Compute a list containing the labels and the parameter values for each type
    of graph that have been used to instantiate graphs
    
    Params
    ------
    classes : list
              list of classes that must be included in the returned list
    Returns
    -------
    l : list
        list containing the labels and the param values used for each graph
        class studied 
    """
    params = [[],[],[],[]]
    for i in range(len(classes)):
        if classes[i] == 'gnp':
            params[i] = list(product(pa.GNP_N, pa.GNP_P, pa.SEEDS))
            params[i].insert(0, ('n', 'p', 'seed'))
        elif classes[i] == 'rrg':
            params[i] = list(product(pa.RR_N, pa.RR_D, pa.SEEDS))
            params[i].insert(0, ('n', 'd', 'seed'))
        elif classes[i] == 'wsg':
            params[i] = list(product(pa.WS_N, pa.WS_P, pa.WS_K, pa.SEEDS))
            params[i].insert(0, ('n', 'p', 'k', 'seed'))
        elif classes[i] == 'bag':
            params[i] = list(product(pa.BA_N, pa.BA_M, pa.SEEDS))
            params[i].insert(0, ('n', 'm', 'seed'))
    return params 
    
def extract_results(classes = ["gnp", "bag", "rrg", "wsg"]):
    """
    Extract and save results for each of the specified classes; for each graph
    class data are extracted from the results of the MIP solver and are stored
    in a CSV file
    
    Params
    ------
    classes : list
              list containing the names of the classes that must be analyzed
    """
    # open a csv output file for each class that we want to analyze
    writers = [csv.writer(open("data/"+classes[i]+".csv", 'w')) for i in range(len(classes))]
    # standard labes
    labels_st = ['name']
    labels_rd = ['time', 'ticks','sol_nodes', 'gap', 'time_lim', 'edges', 'cnnct_cmp', 'avg_clust', 'std_dev_clust']
    # get experiment parameters for the classes specified
    parameters = graph_parameters(classes)
    # write labels in each file
    for i in range(len(classes)):
        writers[i].writerow(labels_st + list(parameters[i].pop(0)) + labels_rd)
    # useful folders path
    resFolder = "mip-results/"
    graphFolder = "graph-instances/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(resFolder) if isfile(join(resFolder, f))]
    files.sort()
    # for each graph in the folder
    for name in files:
        if name[0:3] in classes:
            id = name.split(".")[0]
            fileHandle = open (resFolder + id + ".txt","r" )
            lineList = fileHandle.readlines()
            fileHandle.close()
            graph = nx.read_adjlist(graphFolder + id + ".adjlist")
            row = [id]
            row.extend(list(parameters[classes.index(id[0:3])].pop(0)))
            row.extend(re.findall("\d+\.\d+", lineList[-3]))
            row.append(lineList[-2])
            row.append(lineList[-1])
            row.append(False if float(lineList[-1]) == 0.0 else True)
            row.extend(analyze_graph(graph))
            writers[classes.index(name[0:3])].writerow(row)

if __name__ == "__main__":
    extract_results()
