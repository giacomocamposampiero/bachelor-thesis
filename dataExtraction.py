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
    info.append(nx.radius(graph))
    info.append(nx.diameter(graph))
    return info

def draw(graph):
    nt = Network(notebook=True)
    nt.barnes_hut()
    nt.from_nx(graph)
    nt.show('nx.html')

def get_elapsed_times(string):
    folder = "results/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    writer = csv.writer(open("data.csv", 'w'))
    # for each adjacency list
    for name in files:
        fileHandle = open (folder + name,"r" )
        lineList = fileHandle.readlines()
        fileHandle.close()
        data = re.findall("\d+\.\d+", lineList[-1])
        data.insert(0, name.split(".")[0])
        writer.writerow(data)


def save_results(classes = []):
     

if __name__ == "__main__":
#    print("which graph: ")
#    name = input()
#    graph = nx.read_adjlist("graph-instances/" + name+".adjlist")
#    draw(graph)
     get_elapsed_times()
