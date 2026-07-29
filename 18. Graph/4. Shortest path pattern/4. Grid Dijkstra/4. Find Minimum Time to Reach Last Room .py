import heapq
class Solution(object):
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        minheap = []
        heapq.heappush(minheap, (0, 0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while minheap:
            time, r, c = heapq.heappop(minheap)
            if r == n-1 and c == m-1:
                return dist[r][c]
            if time > dist[r][c]:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    arrival = max(time, moveTime[nr][nc]) + 1
                    if arrival < dist[nr][nc]:
                        dist[nr][nc] = arrival
                        heapq.heappush(minheap, (arrival, nr, nc))
        return -1


            
