# import mean and std deviation from numpy
from numpy import mean
from numpy import std
# import graph utility library
import networkx as nx
# draw graph
import matplotlib.pyplot as plt
from pyvis.network import Network

def analyze(graph, plot=False):
    node_size = nx.number_of_nodes(graph)
    edge_size = nx.number_of_edges(graph)
    num_components = nx.number_connected_components(graph)
    clustering = nx.clustering(graph)
    avg_clustering = mean(list(clustering.values()))
    std_clustering = std(list(clustering.values()))
    diameter = nx.radius(graph)
    radius = nx.diameter(graph)    
