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

class Pair:
    def __init__(self, element, freq):
        self.element = element
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq < other.freq

class Solution(object):
    def topKFrequent(self, nums, k):
        pq = []
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for key, value in hashmap.items():
            heapq.heappush(pq, Pair(key, value))
            if len(pq) > k:
                heapq.heappop(pq)
        
        result = []
        while pq:
            temp = heapq.heappop(pq)
            result.append(temp.element)
        return result

        

