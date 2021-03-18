from pyomo.environ import *
from pyomo.opt import SolverFactory
from graphGeneration import connected_graph

# linear objective function definition
def obj_rule(model):
	return sum(model.x[v] for v in model.vertices)

# contraint applied to edges
def constr_rule(model, u, v):
	return model.x[u] + model.x[v] >= 1

# model definition
def buildmodel():
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

# main function
if __name__ == '__main__':
	import sys
	model = buildmodel()
	opt = SolverFactory('cplex_persistent')
	graph = connected_graph(3, 1)
	print(graph)
	instance = model.create_instance(graph)
	opt.set_instance(instance)
	res = opt.solve(tee=True)
	for p in instance.x:
		print("x[{}] = {}".format(p, value(instance.x[p])))

