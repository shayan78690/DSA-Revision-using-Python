from collections import deque

class Solution(object):

    def dfs(self, node, isConnected, visited):
        visited[node] = True
        n = len(isConnected[node])
        for neighbour in range(n):
            if not visited[neighbour] and isConnected[node][neighbour] == 1:
                self.dfs(neighbour, isConnected, visited)
    
    def bfs(self, node, isConnected, visited):
        q = deque()
        q.append(node)
        visited[node] = True
        while q:
            temp = q.popleft()
            n = len(isConnected[temp])
            for neighbour in range(n):
                if not visited[neighbour] and isConnected[temp][neighbour] == 1:
                    visited[neighbour] = True
                    q.append(neighbour)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        count = 0
        for node in range(n):
            if not visited[node]:
                self.bfs(node, isConnected, visited)
                count += 1
        return count
    
        
