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

def find_dist(i, j, n, adj_list):
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


def get_mean_max_dist(n):
    rep = 100
    max_dists = []
    for i in range(rep):
        p = 0.34
        graph = generate_graph(n = n, p = p)
        adj_list = [[] for _  in range(n)]

        for k in range(n):
            for j in range(n):
                if graph[k][j] == 1:
                    adj_list[k].append(j)
        max_dist = 0
        for k in range(n):
            for j in range(k + 1, n):
                d = find_dist(k, j, n, adj_list)
                if d > max_dist:
                    max_dist = d
        max_dists.append(max_dist)

    return sum(max_dists)/len(max_dists)

x = []
for i in range(10, 201, 10):
    x.append(i)

y = []
for i in x:
    print(i)
    y.append(get_mean_max_dist(i))


plt.plot(x, y)
plt.show()