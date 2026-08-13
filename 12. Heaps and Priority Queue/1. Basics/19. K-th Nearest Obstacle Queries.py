import heapq

class Solution(object):
    def resultsArray(self, queries, k):
        maxheap = []
        result = []
        for x, y in queries:
            dist = abs(x)+abs(y)
            heapq.heappush(maxheap, -dist)
            if len(maxheap) > k:
                heapq.heappop(maxheap)
            if len(maxheap) < k:
                result.append(-1)
            else:
                result.append(-maxheap[0])
        return result
        
