from pyomo.environ import *
from graphGeneration import connected_graph

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
