from collections import deque

class Solution(object):
    def minimumTime(self, n, relations, time):
        adj = [[] for _ in range(n+1)]
        indegree = [0] * (n+1)
        for u, v in relations:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque()
        finishTime = [0] * (n+1)
        for i in range(1, n+1):
            if indegree[i] == 0:
                q.append(i)
                finishTime[i] = time[i-1]

        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                finishTime[neighbour] = max(finishTime[neighbour], finishTime[node]+time[neighbour-1])
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return max(finishTime)
