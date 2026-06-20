import heapq

class Solution:
    def kthSmallest(self, arr, k):
        pq = []
        for a in arr:
            heapq.heappush(pq, -a)
            if len(pq) > k:
                heapq.heappop(pq)
        return -pq[0]
        
