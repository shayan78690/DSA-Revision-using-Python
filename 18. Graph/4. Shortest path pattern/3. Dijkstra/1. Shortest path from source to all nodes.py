import heapq
class Solution:
    def dijkstra(self, V, edges, src):
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [float('inf')] * V
        dist[src] = 0
        
        minheap = []
        heapq.heappush(minheap, (0, src))
        while minheap:
            d, node = heapq.heappop(minheap)
            for neighbour, weight in adj[node]:
                if d + weight < dist[neighbour]:
                    dist[neighbour] = d + weight
                    heapq.heappush(minheap, (d+weight, neighbour))
        return dist
