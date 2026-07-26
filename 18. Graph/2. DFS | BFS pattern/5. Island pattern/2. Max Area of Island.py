class Solution(object):
    def maxAreaOfIsland(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0  or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)
            return area

        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxi = max(maxi, dfs(i, j))
        return maxi



from collections import deque
class Solution(object):
    def maxAreaOfIsland(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()
        def bfs(i, j):
            grid[i][j] = 0
            area = 0
            q.append((i, j))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return area

        maxi = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxi = max(maxi, bfs(i, j))
        return maxi

        
