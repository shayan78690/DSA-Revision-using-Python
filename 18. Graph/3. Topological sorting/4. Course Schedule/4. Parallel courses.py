from collections import deque

def parallelCourses(n, prerequisites):
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for u, v in prerequisites:
        graph[u].append(v)
        indegree[v] += 1
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    courses = 0
    semester = 0
    while q:
        size = len(q)
        semester += 1
        for _ in range(size):
            node = q.popleft()
            courses += 1
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
    return semester if courses == n else -1
