# import mean and std deviation from numpy
from numpy import mean
from numpy import std
# import graph utility library
import networkx as nx
# draw graph
from pyvis.network import Network
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join
# improt regex lib
import re
# import csv lib
import csv

def analyze_graph(graph):
    info = list()
    info.append(nx.number_of_nodes(graph))
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

def draw(graph):
    nt = Network(notebook=True)
    nt.barnes_hut()
    nt.from_nx(graph)
    nt.show('nx.html')

def get_elapsed_times(name, data):
    res = re.findall("\d+\.\d+", data)
    res.insert(0, name)
    return res

def save_results(classes = ["gnp", "bag", "rrg", "wsg"]):
    # open csv file
    writer = csv.writer(open("data.csv", 'w'))
    # write label row
    writer.writerow(['name', 'time', 'ticks','sol_nodes', 'gap', 'time_lim', 'nodes', 'edges', 'cnnct_cmp', 'avg_clust', 'std_dev_clust', 'radius', 'diameter'])
    resFolder = "mip-results/"
    graphFolder = "graph-instances/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(resFolder) if isfile(join(resFolder, f))]
    # for each adjacency list
    for name in files:
        if name[0:3] in classes:
            id = name.split(".")[0]
            fileHandle = open (resFolder + id + ".txt","r" )
            lineList = fileHandle.readlines()
            fileHandle.close()
            graph = nx.read_adjlist(graphFolder + id + ".adjlist")
            row = get_elapsed_times(id, lineList[-3])
            row.append(lineList[-2])
            row.append(lineList[-1])
            row.append(False if float(lineList[-1]) == 0.0 else True)
            row.extend(analyze_graph(graph))
            writer.writerow(row)

if __name__ == "__main__":
#    print("which graph: ")
#    name = input()
#    graph = nx.read_adjlist("graph-instances/" + name+".adjlist")
#    draw(graph)
     save_results()
