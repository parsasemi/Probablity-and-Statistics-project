import math

import networkx as nx
import matplotlib.pyplot as plt


n = 0
probablitiesLonely = []
probablitiesConnected = []
for k in range (0,15):
    num = 0
    sumc = 0
    suml = 0
    connectedOrNot = []
    lonelyNum = []

    n = n + 10
    p = 4/(n)


    for i in range(0,100):
        graph = nx.gnp_random_graph(n,p)
        connectedOrNot.append(nx.is_connected(graph))
        num = 0
        for j in range(0,n):
            if len(graph.adj[j]) == 0 :
                num = num + 1
            lonelyNum.append(num)
    for i in range(0,100):
        sumc = sumc + int(connectedOrNot[i])
        suml = suml + lonelyNum[i]


    probablitiesLonely.append(1-(suml/(len(lonelyNum)*n)))
    probablitiesConnected.append( sumc/len(connectedOrNot))

print("P.Connected: ",probablitiesConnected)
print("P.Lonely: ",probablitiesLonely)

fig, ax = plt.subplots()
ax.plot([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150],probablitiesConnected)
ax.plot([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150],probablitiesLonely)
plt.show()
