
import heapq

class MedianFinder(object):

    def __init__(self):
        # maxheap stores NEGATIVE values to simulate max-heap
        self.maxheap = []
        self.minheap = []

    def addNum(self, num):
        # If maxheap empty or num belongs to maxheap side
        if not self.maxheap or -self.maxheap[0] >= num:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        # Rebalance heaps
        if len(self.maxheap) > len(self.minheap) + 1:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        elif len(self.maxheap) < len(self.minheap):
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -val)

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap):
            return (-self.maxheap[0] + self.minheap[0]) / 2.0
        else:
            return float(-self.maxheap[0])
