import heapq
class Solution(object):
    def reachableNodes(self, edges, maxMoves, n):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w+1))
            adj[v].append((u, w+1))
        dist = [float('inf')] * n
        dist[0] = 0
        minheap = []
        heapq.heappush(minheap, (0, 0))
        while minheap:
            d, node = heapq.heappop(minheap)
            if d > dist[node]:
                continue
            for neighbour, weight in adj[node]:
                if weight + d < dist[neighbour]:
                    dist[neighbour] = weight + d
                    heapq.heappush(minheap, (dist[neighbour], neighbour))
        
        ans = 0
        for d in dist:
            if d <= maxMoves:
                ans += 1
        for u, v, cnt in edges:
            from_u = max(0, maxMoves-dist[u])
            from_v = max(0, maxMoves-dist[v])
            ans += min(cnt, from_u+from_v)
        return ans
        
