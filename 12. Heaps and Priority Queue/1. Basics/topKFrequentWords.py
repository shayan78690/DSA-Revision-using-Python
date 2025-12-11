import heapq
from collections import defaultdict

class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count

    def __lt__(self, other):
        if self.count != other.count:
            return self.count > other.count
        return self.word < other.word


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        freq_map = defaultdict(int)
        for w in words:
            freq_map[w] += 1

        pq = []
        for word, count in freq_map.items():
            heapq.heappush(pq, Pair(word, count))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(pq).word)

        return result
