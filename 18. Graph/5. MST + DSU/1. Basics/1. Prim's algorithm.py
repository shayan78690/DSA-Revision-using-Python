import heapq
class Solution:
    def spanningTree(self, V, edges):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        visited = [False] * V
        minheap = []
        heapq.heappush(minheap, (0, 0))
        mstWeight = 0
        while minheap:
            cost, node = heapq.heappop(minheap)
            if visited[node]:
                continue
            visited[node] = True
            mstWeight += cost
            for neighbour, weight in adj[node]:
                if not visited[neighbour]:
                    heapq.heappush(minheap, (weight, neighbour))
        return mstWeight
