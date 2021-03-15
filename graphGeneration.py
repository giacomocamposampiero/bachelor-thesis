# import random from python std library
from numpy.random import seed
from numpy.random import rand
from numpy.random import randint
# import itertools library
import itertools
# import time library
import time


def generate_graph(dimension, edge_density):
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
	print(edges)

def generate_connected_graph(dimension, edge_density):
	vertices = set({0, 1})
	edges = {(0, 1)}
	seed(rand_seed())
	for ver in range(2, dimension):
		edges.add((ver, randint(low = 0, high = ver)))
		for oth in range(ver):
			if(rand() <= edge_density):
				edges.add((ver, oth))
	print(edges)

def rand_seed():
	tm = int(time.time() * 1000.0)
	return (((tm & 0xff000000) >> 24) +
             ((tm & 0x00ff0000) >>  8) +
             ((tm & 0x0000ff00) <<  8) +
             ((tm & 0x000000ff) << 24))

if __name__ == '__main__':
	import sys
	generate_connected_graph(5, float(sys.argv[1]))

