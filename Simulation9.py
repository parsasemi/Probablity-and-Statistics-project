import random
import numpy as np
from numpy import int16


def generate_graph(n, p):
    if p < 0 or p > 1:
        return None
    graph = np.zeros(shape=(n,n),dtype=int16)
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p:
                graph[i][j] = 1
                graph[j][i] = 1
    return graph

def solve(graph,dimension):
    results = {0:0,1:0}
    for i in range (0,dimension):
        for j in range(i+1,dimension):
            for k in range (j+1, dimension):
                graphlet = graph[np.ix_([i,j,k],[i,j,k])]
                sum = np.sum(graphlet)/2-2
                if sum>=0:
                    results[sum]+=1
    return results
n = 100
p = 0.34
sumLoops = 0
for i in range (0,100):
    print("round:", i)
    taragozari = 0
    graph = generate_graph(n,p)
    sumLoops = solve(graph,n).get(1) + sumLoops

print("expectation Loops:",sumLoops/100)
