# import CPLEX api
import cplex
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join
# import experiment params
import params as pa

if __name__ == "__main__":
    # folder where the lp models are stored
    folder = "mip-instances/"
    output_folder = "mip-results/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each adjacency list
    for name in files:
        id = name.split(".")[0]
        # open an output file for the results of the solution
        f = open(output_folder + id + ".txt", "w")
        # load the problem instance in the solver
        cpx = cplex.Cplex(folder + name)
        # set the solver output stream to the results folder
        cpx.set_results_stream(f)
        # set the time limit for the solution
        cpx.parameters.timelimit.set(pa.T_LIMIT)
        # solve the instance of the problem
        cpx.solve()
        # append to the solution file two other features of the solution
        f.write(str(cpx.solution.get_objective_value()))
        f.write("\n"+str(cpx.solution.MIP.get_mip_relative_gap()))
        # close the solution file
        f.close()
