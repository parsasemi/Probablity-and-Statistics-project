import random


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

def find_dist(i, j):
    seen = [False] * n
    dist = [0] * n
    num_seen = 0
    que = [i]
    while len(que) != 0:
        temp = que.pop(0)
        for k in adj_list[temp]:
            if seen[k]:
                continue
            seen[k] = True
            num_seen += 1
            dist[k] = dist[temp] + 1
            if j == k:
                return dist[j]
            que.append(k)
    return -1

n = 1000
p = 0.0033
graph = generate_graph(n = n, p = p)
adj_list = [[] for _  in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            adj_list[i].append(j)


dists = []
for i in range(n):
    for j in range(i + 1, n):
        d = find_dist(i, j)
        if d == -1:
            continue
        dists.append(d)

print(sum(dists)/len(dists))