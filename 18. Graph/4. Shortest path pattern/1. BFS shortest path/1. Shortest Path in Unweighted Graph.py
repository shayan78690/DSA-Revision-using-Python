from collections import deque
class Solution:
    def shortestPath(self, V, edges, src, dest):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dist = [float('inf')] * V
        q = deque()
        q.append(src)
        dist[src] = 0
        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                if dist[node] + 1 < dist[neighbour]:
                    dist[neighbour] = dist[node] + 1
                    q.append(neighbour)
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist[dest]
        
