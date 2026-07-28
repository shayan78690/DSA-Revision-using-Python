from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        dist = [[float('inf')] * n for _ in range(n)]
        dist[0][0] = 1
        q = deque()
        q.append((0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        while q:
            r, c = q.popleft()
            if r == n-1 and c == n-1:
                return dist[r][c]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return -1
