import networkx as nx

n = 150
p = 0.2
num = 0
sumc = 0
suml = 0
connectedOrNot = []
lonelyNum = []

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

print("P.connected: ",sumc/len(connectedOrNot))
print("P.lonely: ",suml/100*n)
