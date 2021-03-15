# import random from python std library
from numpy.random import seed;
from numpy.random import rand;
# import itertools library
import itertools;
# import time library
import time


def generate_graph(dimension, edge_density):
	threshold  = 1 - edge_density;
	# create the vertices of the graph
	vertices = set(range(dimension));
	# compute all the possibile edges between new graph vertices
	pairs = set(itertools.combinations(vertices, 2));
	# generate a random probability associated to every edge
	probs = random_probs(len(pairs));
	# trim useless edges; the decision to trim an edge is based
	# on its associated probability and the parametric edge density
	edges = set();
	for id,val in enumerate(pairs):
		if probs[id] > threshold:
			edges.add(val);
	print(edges);

def random_probs(length):
	tm = int(time.time() * 1000.0);
	seed(((tm & 0xff000000) >> 24) +
             ((tm & 0x00ff0000) >>  8) +
             ((tm & 0x0000ff00) <<  8) +
             ((tm & 0x000000ff) << 24) );
	return rand(length);

if __name__ == '__main__':
	import sys;
	generate_graph(5, float(sys.argv[1]));

