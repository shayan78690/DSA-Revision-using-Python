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
