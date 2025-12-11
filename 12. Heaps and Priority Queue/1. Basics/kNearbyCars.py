import heapq

class Point:
    def __init__(self, x, y, distSq, idx):
        self.x = x
        self.y = y
        self.distSq = distSq
        self.idx = idx

    # define comparison for min-heap
    def __lt__(self, other):
        return self.distSq < other.distSq


# ----- SAME LOGIC AS JAVA -----
arr = [[3, 3], [5, -1], [-2, 4]]
k = 2

pq = []

for i in range(len(arr)):
    x, y = arr[i]
    distSq = x * x + y * y
    heapq.heappush(pq, Point(x, y, distSq, i))

for _ in range(k):
    p = heapq.heappop(pq)
    print(p.idx)



import heapq

class Point:
    def __init__(self, x, y, distSq, idx):
        self.x = x
        self.y = y
        self.distSq = -distSq   # NEGATIVE → max-heap behavior
        self.idx = idx

    # heap compares distSq (negative)
    def __lt__(self, other):
        return self.distSq < other.distSq


# ----- OPTIMIZED VERSION -----
arr = [[3, 3], [5, -1], [-2, 4]]
k = 2

pq = []

for i in range(len(arr)):
    x, y = arr[i]
    distSq = x * x + y * y
    heapq.heappush(pq, Point(x, y, distSq, i))

    # keep only k closest points
    if len(pq) > k:
        heapq.heappop(pq)

# finally print their indexes
while pq:
    p = heapq.heappop(pq)
    print(p.idx)

