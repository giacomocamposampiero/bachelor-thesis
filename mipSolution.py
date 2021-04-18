# import CPLEX api
import cplex
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    # folder where the lp models are stored
    folder = "mip-instances/"
    output_folder = "mip-results/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each adjacency list
    for name in files:
        id = name.split(".")[0]
        f = open(output_folder + id + ".txt", "w")
        cpx = cplex.Cplex(folder + name)
        # write solving result in corresponding file
        cpx.set_results_stream(f)
        cpx.parameters.timelimit.set(600)
        cpx.solve()
        f.write(str(cpx.solution.get_objective_value()))
        f.write("\n"+str(cpx.solution.MIP.get_mip_relative_gap()))
        f.close()
