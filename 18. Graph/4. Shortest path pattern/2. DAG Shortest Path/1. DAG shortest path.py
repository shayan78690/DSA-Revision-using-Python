from typing import List


class Solution:

    def shortestPath(self, V: int, E: int,
                     edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
        
        visited = [False] * V
        stack = []
        def dfs(node):
            visited[node] = True
            for neighbour, weight in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            stack.append(node)
        
        for i in range(V):
            if not visited[i]:
                dfs(i)
        
        dist = [float('inf')] * V
        dist[0] = 0
        while stack:
            node = stack.pop()
            if dist[node] != float('inf'):
                for neighbour, weight in adj[node]:
                    if dist[node] + weight < dist[neighbour]:
                        dist[neighbour] = dist[node] + weight
        for i in range(V):
            if dist[i] == float('inf'):
                dist[i] = -1
        return dist
        
