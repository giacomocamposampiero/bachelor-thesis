### experiment params

# SEEDS : seeds for random generation, used in every graph
SEEDS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# GNP graph generation
# GNP_N : number of nodes 
# GNP_P : probability for edge generation
GNP_N = [100, 150, 200, 250, 300, 500]
GNP_P = [0.1, 0.3, 0.5, 0.7, 0.9]

# WS_N : number of nodes 
# WS_P : probability of rewiring each edge
# WS_K : number of neighbors joined with every new node 
WS_N = [100, 150, 200, 250, 300, 500]
WS_P = [0.0001, 0.001, 0.01, 0.1, 0.3, 0.5, 0.9]
WS_K = [2, 5, 10, 20, 30]

# RR_N : number of nodes 
# RR_D : degree of each node
RR_N = [100, 150, 200, 250, 300, 500]
RR_D = [2, 3, 4, 5, 7, 10, 20, 30]

# BA_N : number of nodes 
# BA_M : number of edges to attach from a new node to existing nodes
BA_N = [100, 150, 200, 250, 300, 500]
BA_M = [2, 4, 5, 7, 10, 20, 30]

### CPLEX PARAMS

# time limit
T_LIMIT = 1800
