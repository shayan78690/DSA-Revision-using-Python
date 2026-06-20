import heapq

class Solution:
    def findKthLargest(self, nums, k):
        pq = []  

        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)

        return pq[0]

