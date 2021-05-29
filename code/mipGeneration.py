# import pyomo library
from pyomo.environ import *
# import libraries for file reading
from os import listdir
from os.path import isfile, join
# import graph utility library
import networkx as nx

def obj_rule(model):
    """
    Linear objective function definition
    
    Returns
    -------
    f : function
        model objective function to compute the cost of the variables
        the function sum up all the binary variables related to vertices of the 
        graph 
    """
    return sum(model.x[v] for v in model.vertices)

def constr_rule(model, u, v):
    """
    Constraint definition
    
    Returns
    -------
    c : constraint
        constraint that every edge of the graph must satisfy (at least one of 
        the endpoints of the edge must be part of the vertex cover set)        
    """
    return model.x[u] + model.x[v] >= 1

def build_model():
    """
    Model construction

    Returns
    -------    
    m : model
        abstract model of the vertex cover problem
    """
    # model
    model = AbstractModel()
    # sets
    model.vertices = Set()
    model.edges = Set()
    # variables
    model.x = Var(model.vertices, domain=Binary)
    # objective
    model.obj = Objective(rule=obj_rule, sense=minimize)
    # constraints
    model.constrs = Constraint(model.edges, rule=constr_rule)
    return model

# vertex cover instance creation
# the created instance is returned to the caller
def create_instance(graph):
    """
    Vertex cover instance creation
    
    Params
    ------
    graph : dict
            dictionary containing the parameters to build the abstract model
    Returns
    -------
    i : instance
        concrete instance of the problem created using the parametric values
        (edges and nodes) given
    """
    model = build_model()
    return model.create_instance(graph)

if __name__ == "__main__":
    # set the folder where graph instances are stored
    folder = "graph-instances/"
    # build a list of file names contained in that folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each graph instance
    for name in files:
        # get the name of the file without .adjlist extension
        id = name.split(".")[0]
        # build the graph from the adjacency list
        graph = nx.read_adjlist(folder + name)
        # create the mip model for that graph
        instance = create_instance({None: {'vertices': {None: graph.nodes}, 'edges': {None: graph.edges}}})
        # write the mip instance in the dedicated directory 
        instance.write("mip-instances/"+id+".lp")
