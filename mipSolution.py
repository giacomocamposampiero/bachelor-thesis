# import CPLEX api
import cplex
# import libraries for graph file reading
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    # folder where the adjacency list of graphs are stored
    folder = "mip-instances/"
    output_folder = "results/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each adjacency list
    for name in files:
        print("-----------------------")
        print(name)
        id = name.split(".")[0]
        f = open(output_folder + id + ".txt", "w")
        cpx = cplex.Cplex(folder + name)
        #cpx.parameters.tuning.timelimit.set(300.0)
        # prevent cplex from writing output in the shell
        cpx.set_results_stream(None)
        cpx.solve()
        print(cpx.solution.get_quality_metrics())
        f.close()
        if name=='gnp_009.lp':
            break