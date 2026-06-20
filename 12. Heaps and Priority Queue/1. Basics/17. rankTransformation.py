import heapq

class Pair:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx

    def __lt__(self, other):
        return self.val < other.val


class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n = len(arr)
        pq = []

        for i in range(n):
            heapq.heappush(pq, Pair(arr[i], i))

        ans = [0] * n
        prev = None
        rank = 0

        while pq:
            p = heapq.heappop(pq)
            if p.val != prev:
                prev = p.val
                rank += 1
            ans[p.idx] = rank

        return ans
