import heapq
from collections import deque

class Pair:
    def __init__(self, ch, freq):
        self.ch = ch
        self.freq = freq
    
    def __lt__(self, other):
        return self.freq > other.freq

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        hashmap = {}
        for ch in tasks:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        
        maxheap = []
        for ch, freq in hashmap.items():
            heapq.heappush(maxheap, Pair(ch, freq))
        
        time = 0
        cooldown = deque()
        while maxheap or cooldown:
            time += 1
            if maxheap:
                node = heapq.heappop(maxheap)
                node.freq -= 1
                if node.freq > 0:
                    cooldown.append((time + n, node))
            if cooldown and cooldown[0][0] == time:
                _, node = cooldown.popleft()
                heapq.heappush(maxheap, node)
        return time

        
        
