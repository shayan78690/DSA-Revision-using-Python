import heapq
class Solution(object):
    def networkDelayTime(self, times, n, k):
        adj = [[] for _ in range(n+1)]
        for u, v, w in times:
            adj[u].append((v, w))
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        minheap = []
        heapq.heappush(minheap, (0, k))
        while minheap:
            d, node = heapq.heappop(minheap)
            if d > dist[node]:
                continue
            for neighbour, weight in adj[node]:
                if d + weight < dist[neighbour]:
                    dist[neighbour] = d + weight
                    heapq.heappush(minheap, (dist[neighbour], neighbour))
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans
