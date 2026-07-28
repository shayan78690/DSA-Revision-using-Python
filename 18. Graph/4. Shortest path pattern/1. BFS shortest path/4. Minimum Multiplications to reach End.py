from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        dist = [float('inf')] * 1000
        dist[start] = 0
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            if node == end:
                return dist[node]
            for num in arr:
                newnum = (node * num) % 1000
                if dist[node] + 1 < dist[newnum]:
                    dist[newnum] = dist[node] + 1
                    q.append(newnum)
        return -1
