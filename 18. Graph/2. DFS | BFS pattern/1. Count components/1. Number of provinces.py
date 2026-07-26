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
    
        

from collections import deque

class Solution(object):

    def dfs(self, node, visited, adj_list):
        visited[node] = True
        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, visited, adj_list)
    
    def bfs(self, node, visited, adj_list):
        q = deque()
        q.append(node)
        visited[node] = True
        while q:
            temp = q.popleft()
            for neighbour in adj_list[temp]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    q.append(neighbour)

    def findCircleNum(self, isConnected):
        V = len(isConnected)
        adj_list = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if isConnected[i][j] == 1 and i != j:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        visited = [False] * V
        count = 0
        for i in range(V):
            if not visited[i]:
                self.bfs(i, visited, adj_list)
                count += 1
        return count
        
