import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minheap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        else:
            if val > self.minheap[0]:
                heapq.heappop(self.minheap)
                heapq.heappush(self.minheap, val)

        return self.minheap[0]
