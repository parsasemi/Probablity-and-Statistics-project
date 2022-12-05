import random
import numpy as np
from numpy import int16
import matplotlib.pyplot as plt
from numpy import *


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
n = 0
p = 0
exepectation = []
for k in range (0,10):
    sumTaragozari = 0
    n = n + 10
    p = 0.34
    print("n:", n)
    for i in range (0,100):
      print("round:", i)
      graph = generate_graph(n,p)
      sumTaragozari = solve(graph,n).get(1) + sumTaragozari
    exepectation.append(sumTaragozari/100)
    print("expectation taragozari:",sumTaragozari/100)
print("expectation of each n:",exepectation)
x = [10,20,30,40,50,60,70,80,90,100]
default_x_ticks = range(len(x))
plt.plot(default_x_ticks,exepectation)
plt.xticks(default_x_ticks, x)
plt.show()
