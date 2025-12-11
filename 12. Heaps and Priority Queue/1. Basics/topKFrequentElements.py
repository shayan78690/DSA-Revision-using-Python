import heapq
from collections import defaultdict

class Pair:
    def __init__(self, element, freq):
        self.element = element
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.fre

class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = defaultdict(int)
        for x in nums:
            freq_map[x] += 1

        pq = []
        for key in freq_map:
            heapq.heappush(pq, Pair(key, freq_map[key]))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(pq).element)

        return ans



import heapq
from collections import defaultdict

class Pair:
    def __init__(self, element, freq):
        self.element = element
        self.freq = freq

    def __lt__(self, other):
        return self.freq < other.freq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = defaultdict(int)
        for x in nums:
            freq_map[x] += 1

        pq = []

        for element, freq in freq_map.items():
            heapq.heappush(pq, Pair(element, freq))
            if len(pq) > k:
                heapq.heappop(pq)

        result = []
        while pq:
            result.append(heapq.heappop(pq).element)

        return result[::-1]
