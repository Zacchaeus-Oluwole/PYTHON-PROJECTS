# -------------------------------------------------------------------------------------------------------------------------------------------
# tmax: tmax is the maximum time horizon for which the safety measures are to be computed. In the context of the algorithm
#       tmax represents the number of time steps for which the backward iteration is performed.

# n: n is the number of nodes in the graph

# S: Safety value S(t)(u,v)
# S: S is a three-dimensional matrix of size tmax x n x n and represents the dynamic safety matrix.
#    It stores the shortest path distances between nodes at each time step, 
#    where S[t][i][j] represents the shortest path distance from node i to node j at time t.

# C: Dynamic cost of the arcs
# C: C is a three-dimensional matrix of size tmax x n x n and represents the cost matrix.
#    It stores the edge weights between nodes at each time step,
#    where C[t][i][j] represents the weight of the edge from node i to node j at time t.


# Successor: Successor (u, v) = w is defined as the node w succeeding u on the safety path between u and v.
#            By convention Successor (t ) (u, v) = −1 when u=v.
# Successor: Successor is a three-dimensional matrix of size tmax x n x n and represents the successor matrix. 
#            It stores the successor nodes on the shortest path from each node to the destination node at each time step, 
#            where Successor[t][i][j] represents the successor node of node i on the shortest path from node i to node j at time t.

# -----------------------------------------------------------------------------------------------------------------------------------------

# The function DynamicSafety(tmax, n, C, S, Successor) is an algorithm that computes the dynamic safety and successor matrices for a given graph and time horizon. 
# It takes tmax, n, C, S, and Successor as input arguments and updates S and Successor during a backward iteration over the time steps.

# The C matrix is used to compute the shortest path distances between nodes in the graph using the Dijkstra's algorithm, 
# and the computed distances are stored in S. 
# The Successor matrix is updated during the computation of S to store the successor nodes on the shortest path. 
# The backward iteration over time steps then updates the S and Successor matrices to compute the dynamic safety 
# and successor matrices for the given graph and time horizon.

import numpy as np

def DynamicSafety(tmax, n, C, S, Successor):
    V = np.arange(n)
    H = np.zeros(n)
    
    # Forward iteration
    for t in range(tmax):
        for u in V:
            S[t][u][u] = 0
            Successor[t][u][u] = -1
            
            for v in np.delete(V, u):
                S[t][u][v] = -np.inf
                Successor[t][u][v] = u
                
            # Find the shortest path at time T using a static solution
            if t == tmax - 1:
                StaticSafety(S[t], Successor[t])
                
        # Backward iteration
        for t in range(tmax - 2, -1, -1):
            for u in V:
                for v in V:
                    for w in np.where(C[t][u] != 0)[0]:
                        if t+C[t][u][w] < tmax and S[t][u][v] < S[t+C[t][u][w]][w][v] - C[t][u][w]:
                            S[t][u][v] = S[t+C[t][u][w]][w][v] - C[t][u][w]
                            Successor[t][u][v] = w
                            
                S[t][u] = np.minimum(S[t][u], H[t])
                
                if t == 0:
                    break
                
    return S, Successor

def StaticSafety(S, Successor):
    n = S.shape[0]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if S[i][k] + S[k][j] < S[i][j]:
                    S[i][j] = S[i][k] + S[k][j]
                    Successor[i][j] = Successor[i][k]
                    
    return S, Successor


n = 4
tmax = 3
C = np.array([
    [[0, 1, 2, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 0], [1, 0, 0, 0]],
    [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
])
S = np.zeros((tmax, n, n))
Successor = np.zeros((tmax, n, n), dtype=np.int32)

SafetyMatrix, SuccessorMatrix = DynamicSafety(tmax, n, C, S, Successor)
print("Dynamic Safety matrices:\n",SafetyMatrix)
print("Successor matrices:\n",SuccessorMatrix)
