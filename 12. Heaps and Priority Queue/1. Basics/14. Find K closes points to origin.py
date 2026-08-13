import heapq

class Tuple:
    def __init__(self, first, second, dist):
        self.first = first
        self.second = second
        self.dist = dist
    
    def __lt__(self, other):
        return self.dist > other.dist

class Solution(object):
    def kClosest(self, points, k):
        maxheap = []
        for point in points:
            first, second = point
            dist = first*first+second*second
            heapq.heappush(maxheap, Tuple(first, second, dist))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        result = []
        while maxheap:
            node = heapq.heappop(maxheap)
            result.append([node.first, node.second])
        return result
        
