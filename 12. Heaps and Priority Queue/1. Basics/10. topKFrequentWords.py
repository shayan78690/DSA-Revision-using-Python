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


import heapq

class Pair:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
    def __lt__(self, other):
        return self.freq < other.freq if self.freq != other.freq else self.ch > other.ch

class Solution(object):
    def topKFrequent(self, words, k):
        minheap = []
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0)+1
        for key, value in hashmap.items():
            heapq.heappush(minheap, Pair(key, value))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        result = [0] * k
        index = k-1
        while minheap:
            temp = heapq.heappop(minheap)
            result[index] = temp.ch
            index -= 1
        return result
        
        
