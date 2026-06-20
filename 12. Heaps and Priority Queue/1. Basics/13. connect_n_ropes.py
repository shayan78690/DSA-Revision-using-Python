import heapq

class Solution:
    def minCost(self, arr):
        pq = []
        for a in arr:
            heapq.heappush(pq, a)
        
        cost = 0
        while len(pq) > 1:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            s = first + second
            cost += s
            heapq.heappush(pq, s)

        return cost
