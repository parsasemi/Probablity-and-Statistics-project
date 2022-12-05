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


n = 1000
p = 0.003

graph = generate_graph(n = n, p = p)

ans = []
for i in range(n):
    adj = []
    for j in range(n):
        if graph[i][j] == 1:
            adj.append(j)
    # adj = neighbors of i
    s = 0
    for j in adj:
        for k in adj:
            if j == k:
                #so that only the neighbors count
                continue
            if graph[j][k] == 1:
                s += 1

    ans.append(s/2)
print(sum(ans)/len(ans))