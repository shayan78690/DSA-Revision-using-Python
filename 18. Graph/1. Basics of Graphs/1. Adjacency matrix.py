V = 4

edges = [
    (0,1),
    (0,2),
    (1,2),
    (1,3)
]

graph = [[0] * V for _ in range(V)]

for u, v in edges:
    graph[u][v] = 1
    graph[v][u] = 1

for row in graph:
    print(row)
