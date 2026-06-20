import heapq

class Tuple:
    def __init__(self, first, second, sum_):
        self.first = first
        self.second = second
        self.sum = sum_

    def __lt__(self, other):
        # make heapq behave like Java's max-heap comparator (larger sum = higher priority)
        return self.sum > other.sum


class Solution:
    def topKSumPairs(self, a, b, k):
        """
        :type a: List[int]
        :type b: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not a or not b or k <= 0:
            return []

        n = len(a)
        m = len(b)

        a.sort()
        b.sort()

        pq = []
        start_j = max(0, m - k)
        for j in range(m - 1, start_j - 1, -1):
            heapq.heappush(pq, Tuple(n - 1, j, a[n - 1] + b[j]))

        result = []
        while k > 0 and pq:
            t = heapq.heappop(pq)
            result.append(t.sum)
            if t.first - 1 >= 0:
                heapq.heappush(pq, Tuple(t.first - 1, t.second, a[t.first - 1] + b[t.second]))
            k -= 1

        return result

