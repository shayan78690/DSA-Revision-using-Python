import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap) > 1:
            first = -heapq.heappop(maxheap)
            second = -heapq.heappop(maxheap)
            if first != second:
                new_weight = first-second
                heapq.heappush(maxheap, -new_weight)
        return -maxheap[0] if maxheap else 0
