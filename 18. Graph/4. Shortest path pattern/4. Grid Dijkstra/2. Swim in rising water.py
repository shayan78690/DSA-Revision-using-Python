import heapq
class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = grid[0][0]
        minheap = []
        heapq.heappush(minheap, (grid[0][0], 0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while minheap:
            currTime, r, c = heapq.heappop(minheap)
            if r == n-1 and c == n-1:
                return dist[r][c]
            if currTime > dist[r][c]:
                continue
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    newTime = max(currTime, grid[nr][nc])
                    if newTime < dist[nr][nc]:
                        dist[nr][nc] = newTime
                        heapq.heappush(minheap, (newTime, nr, nc))
        return -1
            
