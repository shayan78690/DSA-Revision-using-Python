class Solution:
    def dfs(self, adj):
        result = []
        visited = [False] * len(adj)
        self.DFS(0, adj, visited, result)
        return result
    
    def DFS(self, node, adj, visited, result):
        visited[node] = True
        result.append(node)
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.DFS(neighbour, adj, visited, result)
