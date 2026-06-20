import heapq

class Pair:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq > other.freq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap = {}
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        maxheap = []
        for ch, freq in hashmap.items():
            heapq.heappush(maxheap, Pair(ch, freq))
        
        ans = []
        while maxheap:
            p = heapq.heappop(maxheap)
            ans.append(p.ch * p.freq)
        return "".join(ans)
