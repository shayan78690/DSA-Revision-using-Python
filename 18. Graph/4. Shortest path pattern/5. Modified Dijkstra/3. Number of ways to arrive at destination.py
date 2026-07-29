import heapq
class Solution(object):
    def countPaths(self, n, roads):
        mod = 10**9+7
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        dist = [float('inf')] * n
        dist[0] = 0
        count = [0] * n
        count[0] = 1
        minheap = []
        heapq.heappush(minheap, (0, 0))
        while minheap:
            d, node = heapq.heappop(minheap)
            if d > dist[node]:
                continue
            for neighbour, weight in adj[node]:
                if d + weight < dist[neighbour]:
                    dist[neighbour] = d + weight
                    count[neighbour] = count[node]
                    heapq.heappush(minheap, (d+weight, neighbour))
                elif d + weight == dist[neighbour]:
                    count[neighbour] = (count[neighbour] + count[node]) % mod
        return count[n-1]
        
