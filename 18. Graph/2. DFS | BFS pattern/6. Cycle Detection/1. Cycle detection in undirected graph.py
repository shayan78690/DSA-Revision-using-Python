class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V

        def dfs(node, parent):
            visited[node] = True

            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True

            return False

        for i in range(V):
            if not visited[i]:
                if dfs(i, -1):
                    return True

        return False



from collections import deque

class Solution:
    def isCycle(self, V, edges):
        adj = [[] for _ in range(V)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * V
        
        def bfs(src):
            q = deque()
            q.append((src, -1))
            visited[src] = True
            while q:
                node, parent = q.popleft()
                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        q.append((neighbour, node))
                    elif neighbour != parent:
                        return True
            return False
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True

        return False
