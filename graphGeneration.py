# import random from python numpy library
from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
# import graph utility library
import networkx as nx
# import itertools library
import itertools
# draw graph
import matplotlib.pyplot as plt

def graph(dimension, edge_density, rseed):
    # define a new graph instance
    G = nx.Graph()
    # create the vertices of the graph
    vertices = range(dimension)
    G.add_nodes_from(vertices)
    # compute all the possibile edges between new graph vertices
    pairs = set(itertools.combinations(vertices, 2))
    # generate a random probability associated to every edge
    seed(rseed)
    probs = rand(len(pairs))
    # trim useless edges; the decision to trim an edge is based
    # on its associated probability and on the parametric edge density
    edges = set()
    for id,val in enumerate(pairs):
        if probs[id] <= edge_density:
            edges.add(val)
    G.add_edges_from(edges)
    return G

def connected_graph(dimension, edge_density, rseed):
    # init vertices and edges
    vertices = {0}
    edges = set()
    # random seed generation
    seed(rseed)
    for ver in range(1, dimension):
        # add the new vertex to the graph
        vertices.add(ver)
        # set at least one random edge
        # necessary for the generation of spanning trees
        fixed = randint(low = 0, high = ver)
        edges.add((ver, fixed))
        # generate the probabilities for remaining vertices
        for oth in range(ver):      
            # other edges generation based on probability
            # duplicates edges are not added to the set
            if(rand() <= edge_density):
                edges.add((ver, oth))
    return {None: {'vertices': {None: vertices}, 'edges': {None: edges}}}
	
if __name__ == "__main__":
    gr = graph(150, 0.01, 2)
    nx.draw(gr, with_labels=True)
    plt.savefig("path.png")
    print(len(list(nx.connected_components(gr))))
    
    
    
    
    
    
    
    
    
    
    
