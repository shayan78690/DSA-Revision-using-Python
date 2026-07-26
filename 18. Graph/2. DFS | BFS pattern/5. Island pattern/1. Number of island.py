class Solution(object):
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count




from collections import deque
class Solution(object):
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(r, c):
            q.append((r, c))
            grid[r][c] = "0"
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        q.append((nr, nc))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count
        
