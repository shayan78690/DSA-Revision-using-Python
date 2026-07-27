class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        visited = [False] * V
        pathVisited = [False] * V
        
        def dfs(node):
            visited[node] = True
            pathVisited[node] = True
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour):
                        return True
                elif pathVisited[neighbour]:
                    return True
            pathVisited[node] = False
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i):
                    return True
        return False
