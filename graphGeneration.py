# import graph utility library
import networkx as nx
# generation parameters
import params as pr

def save_graph(graph, type, id):
    nx.write_adjlist(graph, "graphInstances/"+type+"_{0:03d}.adjlist".format(id))
    
def graph_generator(generator, ns, seeds, ps = None, ks = None, ds = None, ms = None):
    """
    """
    graphs = list()
    # for each graph dimension
    for n in ns:
        # for each random seed
        for seed in seeds:
            if(ds is not None):
                # regular graph
                for d in ds:
                    graphs.append(generator(d, n, seed))
                    typ = "rr"
            elif(ms is not None):
                # Barabási–Albert graph
                for m in ms:
                    graphs.append(generator(n, m, seed))
                    typ = "ba"
            else:
                for p in ps:
                    if(ks is not None):
                        # Watts–Strogatz small-world graph
                        for k in ks:    
                            graphs.append(generator(n, k, p, seed))
                            typ = "ws"
                    else:
                        # Erdős-Rényi graph 
                        graphs.append(generator(n, p, seed))
                        typ = "gnp"
    for index in range(len(graphs)):
        save_graph(graphs[index], typ, index)                                 

if __name__ == "__main__":
    graph_generator(generator = nx.gnp_random_graph, ns = pr.GNP_N, seeds = pr.SEEDS, ps = pr.GNP_P) 
    graph_generator(generator = nx.watts_strogatz_graph, ns = pr.WS_N, seeds = pr.SEEDS, ps = pr.WS_P, ks = pr.WS_K)
    graph_generator(generator = nx.random_regular_graph, ns = pr.RR_N, seeds = pr.SEEDS, ds = pr.RR_D)
    graph_generator(generator = nx.barabasi_albert_graph, ns = pr.BA_N, seeds = pr.SEEDS, ms = pr.BA_M)
