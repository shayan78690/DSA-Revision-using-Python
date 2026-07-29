import heapq

class Solution(object):
    def minimumTime(self, grid):
        n, m = len(grid), len(grid[0])
        if n > 1 and m > 1 and grid[0][1] > 1 and grid[1][0] > 1:
            return -1
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
                    arrivalTime = time + 1
                    if arrivalTime < grid[nr][nc]:
                        arrivalTime = grid[nr][nc] + (grid[nr][nc]-arrivalTime) % 2
                    if arrivalTime < dist[nr][nc]:
                        dist[nr][nc] = arrivalTime
                        heapq.heappush(minheap, (arrivalTime, nr, nc))
        return -1
                    
