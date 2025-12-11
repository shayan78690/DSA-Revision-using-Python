
import heapq

class Pair:
    def __init__(self, val, i, j):
        self.val = val  # value
        self.i = i      # which array
        self.j = j      # index in that array

    # For min-heap behavior
    def __lt__(self, other):
        return self.val < other.val


class Solution(object):
    def mergeKArrays(self, arr, K):
        """
        :type arr: List[List[int]]
        :type K: int
        :rtype: List[int]
        """
        pq = []

        # Step 1: Push the first element of each array
        for i in range(len(arr)):
            heapq.heappush(pq, Pair(arr[i][0], i, 0))

        ans = []

        # Step 2: Pop smallest, and push its next element
        while pq:
            p = heapq.heappop(pq)
            ans.append(p.val)

            if p.j + 1 < len(arr[p.i]):
                heapq.heappush(
                    pq,
                    Pair(arr[p.i][p.j + 1], p.i, p.j + 1)
                )

        return ans
