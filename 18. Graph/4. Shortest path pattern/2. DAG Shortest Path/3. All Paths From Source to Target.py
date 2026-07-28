class Solution(object):
    def allPathsSourceTarget(self, graph):
        V = len(graph)
        adj = [[] for _ in range(V)]
        for u in range(V):
            for v in graph[u]:
                adj[u].append(v)
        ans = []
        def dfs(node, path):
            if node == V-1:
                ans.append(path[:])
                return
            for neighbour in adj[node]:
                path.append(neighbour)
                dfs(neighbour, path)
                path.pop()
        path = [0]
        dfs(0, path)
        return ans
        
