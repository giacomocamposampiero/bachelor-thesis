# import graph utility library
import networkx as nx
# generation parameters
import params as pr
# import cartesian product method
from itertools import product

def save_graph(graph, g_type, id):
    """ 
    Save graph as an adjency list in the folder "graph-instance"
    Name of the files are formatted as: TYPE "_" 3*DIGIT(id) ".adjlist"
        
    Parameters
    ----------
    graph : graph
            networkx graph to be saved
    type  : string
            type of graph
    id    : int
            integer id associated to the graph
    Returns
    -------
    None
    """
    nx.write_adjlist(graph, "graph-instances/"+g_type+"_{0:05d}.adjlist".format(id))

def graph_generator(generator, g_type, *par):
    """
    Generate a graph using the corresponding generator function and a list of 
    parameters of variable size and save it in the disk
    
    Parameters
    ----------
    generator : function
                function of networkx lib to generate the graph
    g_type    : string
                type of graph
    *par      : variable number of parameters
                parameters for the generator
    Returns
    -------
    None
    """
    index = 0
    # for each possible combination of parameters
    for comb in product(*par):
        # generate the graph
        graph = generator(*comb)
        # save the graph
        save_graph(graph, g_type, index)
        # increase the numeric index
        index += 1

if __name__ == "__main__":
    #graph_generator(nx.gnp_random_graph, 'gnp', pr.GNP_N, pr.GNP_P, pr.SEEDS)
    #graph_generator(nx.watts_strogatz_graph, 'wsg', pr.WS_N, pr.WS_K, pr.WS_P, pr.SEEDS)
    graph_generator(nx.random_regular_graph, 'rrg', pr.RR_D, pr.RR_N, pr.SEEDS)
    #graph_generator(nx.barabasi_albert_graph, 'bag', pr.BA_N, pr.BA_M, pr.SEEDS)
