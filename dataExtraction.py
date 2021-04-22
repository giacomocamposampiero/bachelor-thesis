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
    info = list()
    info.append(nx.number_of_edges(graph))
    info.append(nx.number_connected_components(graph))
    clustering = nx.clustering(graph)
    info.append(mean(list(clustering.values())))
    info.append(std(list(clustering.values())))
    if(nx.is_connected(graph)):
        rad = [nx.radius(graph), nx.diameter(graph)]
    else:
        rad = [-1, -1]
    info.extend(rad)
    return info
    
def graph_parameters(classes):
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
    
def save_results(classes = ["gnp", "bag", "rrg", "wsg"]):
    # open csv file
    writers = [csv.writer(open("data/"+classes[i]+".csv", 'w')) for i in range(len(classes))]
    # label row
    labels_st = ['name']
    labels_rd = ['time', 'ticks','sol_nodes', 'gap', 'time_lim', 'edges', 'cnnct_cmp', 'avg_clust', 'std_dev_clust', 'radius', 'diameter']
    # get experiment parameters
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
            row.append(re.findall("\d+\.\d+", lineList[-3]))
            row.append(lineList[-2])
            row.append(lineList[-1])
            row.append(False if float(lineList[-1]) == 0.0 else True)
            row.extend(analyze_graph(graph))
            writers[classes.index(name[0:3])].writerow(row)

if __name__ == "__main__":
    save_results()
