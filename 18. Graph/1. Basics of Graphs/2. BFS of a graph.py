from collections import deque
class Solution:
    def bfs(self, adj):
        q = deque()
        visited = [False] * len(adj)
        q.append(0)
        visited[0] = True
        result = []
        while q:
            node = q.popleft()
            result.append(node)
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)
        return result
