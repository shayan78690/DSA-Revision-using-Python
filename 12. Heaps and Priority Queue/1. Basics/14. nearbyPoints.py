import heapq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distSq = x * x + y * y

    def __lt__(self, other):
        return self.distSq < other.distSq


class Solution(object):
    def kClosest(self, points, k):
        pq = []

        for x, y in points:
            heapq.heappush(pq, Point(x, y))

        ans = []
        for _ in range(k):
            p = heapq.heappop(pq)
            ans.append([p.x, p.y])

        return ans



import heapq

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distSq = -(x * x + y * y)

    def __lt__(self, other):
        return self.distSq < other.distSq


class Solution(object):
    def kClosest(self, points, k):
        pq = []  

        for x, y in points:
            heapq.heappush(pq, Point(x, y))

            if len(pq) > k:
                heapq.heappop(pq)

        ans = []
        while pq:
            p = heapq.heappop(pq)
            ans.append([p.x, p.y])

        return ans


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
