# import random from python std library
from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
from numpy.random import uniform
# import itertools library
import itertools
# import time library
import time

def graph(dimension, edge_density):
	# create the vertices of the graph
	vertices = set(range(dimension))
	# compute all the possibile edges between new graph vertices
	pairs = set(itertools.combinations(vertices, 2))
	# generate a random probability associated to every edge
	seed(rand_seed())
	probs = rand(len(pairs))
	# trim useless edges; the decision to trim an edge is based
	# on its associated probability and the parametric edge density
	edges = set()
	for id,val in enumerate(pairs):
		if probs[id] <= edge_density:
			edges.add(val)
	return {None: {'vertices': vertices, 'edges': edges}}

def connected_graph(dimension, edge_density):
	# init vertices and edges
	vertices = {0}
	edges = set()
	# random seed generation
	seed(rand_seed())
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

def rand_seed():
	tm = int(time.time() * 1000.0)
	return (((tm & 0xff000000) >> 24) +
             ((tm & 0x00ff0000) >>  8) +
             ((tm & 0x0000ff00) <<  8) +
             ((tm & 0x000000ff) << 24))

if __name__ == '__main__':
	import sys
	x = generate_connected_graph(25, float(sys.argv[1]))
	y = generate_graph(25, float(sys.argv[1]))
	print(len(x[None]["edges"]));
#	print(len(y[None]["edges"]));


