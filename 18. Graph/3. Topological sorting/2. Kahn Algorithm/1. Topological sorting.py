from collections import deque
class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
        indegree = [0] * V
        for u in range(V):
            for v in adj[u]:
                indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return ans
