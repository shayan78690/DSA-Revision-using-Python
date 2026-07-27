class Solution(object):
    def isBipartite(self, graph):
        V = len(graph)
        def dfs(node):
            for neighbour in graph[node]:
                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[node]
                    if not dfs(neighbour):
                        return False
                elif color[node] == color[neighbour]:
                    return False
            return True
        color = [-1] * V
        for i in range(V):
            if color[i] == -1:
                color[i] = 0
                if not dfs(i):
                    return False
        return True



from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        V = len(graph)
        color = [-1] * V
        def bfs(start):
           q = deque()
           q.append(start) 
           color[start] = 0
           while q:
                node = q.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        q.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False
           return True
        
        for i in range(V):
            if color[i] == -1:
                if not bfs(i):
                    return False
        return True
        
