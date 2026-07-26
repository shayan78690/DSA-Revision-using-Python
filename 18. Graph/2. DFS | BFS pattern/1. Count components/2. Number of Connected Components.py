from collections import deque

class Solution:
    def countConnected(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [False] * V
        count = 0
        for i in range(V):
            if not visited[i]:
                count += 1
                self.bfs(i, adj_list, visited)
        
        return count
    
    def dfs(self, node, adj_list, visited):
        visited[node] = True
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj_list, visited)
    
    def bfs(self, node, adj_list, visited):
        q = deque()
        q.append(node)
        visited[node] = True
        while q:
            temp = q.popleft()
            for neighbour in adj_list[temp]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
