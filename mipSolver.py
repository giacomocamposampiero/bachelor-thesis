# import CPLEX api
import cplex 

if __name__ == "__main__":
    # folder where the adjacency list of graphs are stored
    folder = "mipInstances/"
    # build a list of file names contained in the folder
    files = [f for f in listdir(folder) if isfile(join(folder, f))]
    # for each adjacency list
    for name in files:
        f = open(folder+name, "w")
        cpx = cplex.Cplex(name)     
        cpx.set_results_stream(f)
        cpx.solve()
