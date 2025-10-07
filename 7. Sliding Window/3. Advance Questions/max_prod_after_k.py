import heapq

class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        mod = 1000000007
        minheap = []
        
        for i in range(n):
            heapq.heappush(minheap, nums[i])
        
        for i in range(k):
            smallest = heapq.heappop(minheap)
            smallest = smallest + 1
            heapq.heappush(minheap, smallest)
        
        prod = 1
        while minheap:
            prod = (prod * heapq.heappop(minheap)) % mod
        
        return prod

        