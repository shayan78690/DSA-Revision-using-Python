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
        freq_map = {}
        for ch in s:
            freq_map[ch] = freq_map.get(ch, 0) + 1
        
        max_heap = []
        for ch, freq in freq_map.items():
            heapq.heappush(max_heap, Pair(ch, freq))
        
        ans = []
        while max_heap:
            p = heapq.heappop(max_heap)
            ans.append(p.ch * p.freq)
        return "".join(ans)