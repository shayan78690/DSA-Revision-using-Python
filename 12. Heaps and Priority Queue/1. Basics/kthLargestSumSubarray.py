import heapq

class Solution:
    def kthLargest(self, arr, k):
        n = len(arr)
        pq = []  
        
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]
                heapq.heappush(pq, sum_)
                
                if len(pq) > k:
                    heapq.heappop(pq)
        
        return pq[0]
