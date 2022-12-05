import random

import networkx as nx
import numpy as np
from numpy import int16
import matplotlib.pyplot as plt
from numpy import *


n = 0
p = 0
exepectation = []
N = []
Y = []
for k in range (0,24):
    n = n + 50
    N.append(n)
    p = 1/n
    print("n:", n)
    sumTriangles = 0
    for i in range (0,100):
      print("round:", i)

      graph = nx.gnp_random_graph(n, p)
      trianglelsNum = 0
      map = nx.triangles(graph)
      for node in range (0,n):
        trianglelsNum = trianglelsNum + map.get(node)

      trianglelsNum = trianglelsNum / 3
      sumTriangles = sumTriangles+trianglelsNum

    exepectation.append(sumTriangles/100)


# print("expectation of each n:",exepectation)
# for i in range(0,24):
#     if i==0:
#         Y.append(exepectation[i])
#     else:
#       Y.append((exepectation[i] + Y[i-1])/(i+1))

default_x_ticks = range(len(N))
# plt.plot(default_x_ticks,Y)
# plt.xticks(default_x_ticks, N)
x = []
for i in range(50, 1201, 50):
    x.append(i)


plt.plot(x,exepectation)
plt.show()
