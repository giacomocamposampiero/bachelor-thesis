from graphGeneration import connected_graph
from vertexCover import create_instance
import params

# main
if __name__ == "__main__":
	id = 0
	for dim in params.DIME:
		for den in params.DENS:
			for sed in params.SEED:
				graph = connected_graph(dim, den, sed)
				instance = create_instance(graph)
				instance.write("instances/instance_{0:04d}.lp".format(id))
				id += 1

