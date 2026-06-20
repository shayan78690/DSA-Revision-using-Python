import heapq
from collections import deque

class TaskNode:
    def __init__(self, freq, task):
        self.freq = freq
        self.task = task

    # Max heap behavior
    def __lt__(self, other):
        return self.freq > other.freq


class Solution(object):
    def leastInterval(self, tasks, n):
        # Build frequency map
        freq_map = {}
        for ch in tasks:
            freq_map[ch] = freq_map.get(ch, 0) + 1

        # Create max heap
        maxheap = []
        for ch, f in freq_map.items():
            heapq.heappush(maxheap, TaskNode(f, ch))

        time = 0
        cooldown = deque()   # (available_time, TaskNode)

        while maxheap or cooldown:
            time += 1

            # Execute highest freq task
            if maxheap:
                node = heapq.heappop(maxheap)
                node.freq -= 1
                if node.freq > 0:
                    cooldown.append((time + n, node))

            # Cooldown finished?
            if cooldown and cooldown[0][0] == time:
                _, node = cooldown.popleft()
                heapq.heappush(maxheap, node)

        return time
