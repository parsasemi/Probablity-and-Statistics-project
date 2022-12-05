import random
import matplotlib.pyplot as plt


def generate_graph(n, p):
    if p < 0 or p > 1:
        return None
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p:
                arr[i][j] = 1
                arr[j][i] = 1
    return arr



import networkx as nx
from networkx import degree, degree_histogram

n = 1000
p = 0.00016
edgeNumbers=[]


sociableNum = 0
sumSociableNum = 0
for j in range(0,10):
    sociableNum = 0
    g = nx.gnp_random_graph(n, p)
    edgeNumbers = []
    for i in range(0, 1000):
        edgeNumbers.append(g.degree(i))

    L = len(g.edges) / n

    for i in range (0,1000):
        if edgeNumbers[i]>L :
            sociableNum = sociableNum+1
    sumSociableNum = sumSociableNum+sociableNum

expectation = sumSociableNum/10

print(expectation)




sumTotal = [0] * n

for i in range(0,10):
    graph = generate_graph(n, p)
    num_neighbors = [0] * n
    for j in range(0,n):
        num_neighbors[j] = sum(graph[j])
        sumTotal[j] = sumTotal[j] + num_neighbors[j]


for i in range (0,n):
    sumTotal[i] = sumTotal[i] / 10

plt.hist(sumTotal, bins = 10)
plt.show()

