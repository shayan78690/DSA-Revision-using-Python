from collections import deque

class Solution:
    def isPossible(self, n, pre):
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for u, v in pre:
            adj[v].append(u)
            indegree[u] += 1
            
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return completed == n
