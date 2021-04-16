# import pyomo library
from pyomo.environ import *
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join
# import graph utility library
import networkx as nx

# linear objective function definition
def obj_rule(model):
    return sum(model.x[v] for v in model.vertices)

# contraint applied to edges
def constr_rule(model, u, v):
    return model.x[u] + model.x[v] >= 1

# model definition
def build_model():
    # model
    model = AbstractModel()
    # sets
    model.vertices = Set()
    model.edges = Set()
    # variables
    model.x = Var(model.vertices, domain=NonNegativeIntegers, bounds=(0,1))
    # objective
    model.obj = Objective(rule=obj_rule, sense=minimize)
    # constraints
    model.constrs = Constraint(model.edges, rule=constr_rule)
    return model

# vertex cover instance creation
# the created instance is returned to the caller
def create_instance(graph):
    model = build_model()
    return model.create_instance(graph)

if __name__ == "__main__":
    # folder where the adjacency list of graphs are stored
    folder = "graph-instances/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each adjacency list
    for name in files:
        # get the name of the file without .adjlist format
        id = name.split(".")[0]
        # build the graph from the matrix
        graph = nx.read_adjlist(folder + name)
        # create the mip model
        instance = create_instance({None: {'vertices': {None: graph.nodes}, 'edges': {None: graph.edges}}})
        # write the mip model in the dedicated directory 
        instance.write("mip-instances/"+id+".lp")
