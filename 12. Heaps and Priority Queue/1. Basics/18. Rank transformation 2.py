import heapq

class Pair:
    def __init__(self, element, index):
        self.element = element
        self.index = index

    def __lt__(self, other):
        return (
            self.element < other.element
            if self.element != other.element
            else self.index < other.index
        )

class Solution:
    def replaceWithRank(self, arr):
        minheap = []

        for i in range(len(arr)):
            heapq.heappush(minheap, Pair(arr[i], i))

        rank = 0

        while minheap:
            node = heapq.heappop(minheap)
            idx = node.index

            arr[idx] = rank
            rank += 1

        return arr
