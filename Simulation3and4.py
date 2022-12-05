import random

n = 3000
p = 0.01


def generate_graph(n, p):
    if p < 0 or p > 1:
        return None
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p:
                graph[i][j] = 1
                graph[j][i] = 1
    return graph


sumTaragozari = 0
sumRace = 0
for fuck in range(0, 5):
    print("round:",fuck)
    graph = generate_graph(n, p)
    taragozari = 0
    race = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if graph[i][j] == 1 & graph[i][k] == 1 & graph[j][k] == 1:
                    taragozari = taragozari + 1
                elif graph[i][j] == 1 & graph[i][k] == 1 & graph[j][k] == 0:
                    race = race + 1
                elif graph[i][j] == 1 & graph[i][k] == 0 & graph[j][k] == 1:
                    race = race + 1
                elif graph[i][j] == 0 & graph[i][k] == 1 & graph[j][k] == 1:
                    race = race + 1
    sumTaragozari = taragozari + sumTaragozari
    sumRace = sumRace + race

print("taragozari", taragozari)
print("race:", race)
print("expectation taragozari:",sumTaragozari/5)
print("expectation race:",sumRace/5)
