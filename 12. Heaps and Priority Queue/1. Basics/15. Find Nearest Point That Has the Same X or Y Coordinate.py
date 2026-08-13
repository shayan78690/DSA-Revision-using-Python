import heapq

class Pair:
    def __init__(self, index, dist):
        self.index = index
        self.dist =  dist
    def __lt__(self, other):
        return self.dist < other.dist if self.dist != other.dist else self.index < other.index
class Solution(object):
    def nearestValidPoint(self, x, y, points):
        n = len(points)
        minheap = []
        for i in range(n):
            a, b = points[i]
            if a == x or b == y:
                dist = abs(a-x)+abs(b-y)
                heapq.heappush(minheap, Pair(i, dist))
        
        return minheap[0].index if minheap else -1

        
