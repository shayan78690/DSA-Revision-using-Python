from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i) # because the course which has no dependency will be processed first
        
        processed = 0
        while q:
            node = q.popleft()
            processed += 1
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        return processed == numCourses 
