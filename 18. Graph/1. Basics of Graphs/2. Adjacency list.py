V = 4

edges = [
    (0,1),
    (0,2),
    (1,2),
    (1,3)
]

graph = [[] for _ in range(V)]

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(graph)
