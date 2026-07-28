import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        adj = [[] for _ in range(n)]
        for (u, v), p in zip(edges, succProb):
            adj[u].append((v, p))
            adj[v].append((u, p))
        dist = [0] * n
        dist[start_node] = 1
        maxheap = []
        heapq.heappush(maxheap, (-1.0, start_node))
        while maxheap:
            neg_prob, node = heapq.heappop(maxheap)
            prob = -neg_prob
            if prob < dist[node]:
                continue
            for neighbour, p in adj[node]:
                if prob * p > dist[neighbour]:
                    dist[neighbour] = prob * p
                    heapq.heappush(maxheap, (-dist[neighbour], neighbour))
        return dist[end_node]
