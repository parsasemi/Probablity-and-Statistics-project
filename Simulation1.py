import networkx as nx

n = 1000
p = 0.0034
sum = 0.0
sumarray = []

for i in range(0, 10):
    g = nx.gnp_random_graph(n, p)
    print(len(g.edges))
    sum = len(g.edges) + sum
    sumarray.append(sum)

expected = sum / 10
print("Sum Array: ", sumarray)
print("Expected: ", expected)

Error = (3000 - (sum / 10)) / 3000
if Error > 0.05:
    print("Expected value is not in the range of 5% error")
    print("Error:",Error)
