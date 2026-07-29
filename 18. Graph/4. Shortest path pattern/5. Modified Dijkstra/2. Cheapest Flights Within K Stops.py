import heapq
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))
        
        minheap = []
        heapq.heappush(minheap, (0, src, 0))
        while minheap:
            d, node, stops = heapq.heappop(minheap)
            if node == dst:
                return d
            if stops > k:
                continue
            for neighbour, price in adj[node]:
                heapq.heappush(minheap, (price + d, neighbour, stops+1))
        return -1


from collections import deque
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        adj = [[] for _ in range(n)]
        for u, v, p in flights:
            adj[u].append((v, p))
        
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque()
        q.append((0, src, 0))
        while q:
            d, node, stops = q.popleft()
            if stops > k:
                continue
            for neighbour, price in adj[node]:
                newcost = price + d
                if newcost < dist[neighbour]:
                    dist[neighbour] = newcost
                    q.append((newcost, neighbour, stops+1))
        return -1 if dist[dst] == float('inf') else dist[dst]
