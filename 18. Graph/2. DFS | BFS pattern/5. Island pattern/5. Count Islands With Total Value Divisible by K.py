class Solution(object):
    def countIslands(self, grid, k):
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0
            s = grid[i][j]
            grid[i][j] = 0
            s += dfs(i+1, j)
            s += dfs(i-1, j)
            s += dfs(i, j+1)
            s += dfs(i, j-1)
            return s

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total = dfs(i, j)
                    if total % k == 0:
                        count += 1
        return count



from collections import deque

class Solution(object):
    def countIslands(self, grid, k):
        n, m = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = deque()
            q.append((sr, sc))

            total = grid[sr][sc]
            grid[sr][sc] = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0:
                        total += grid[nr][nc]
                        q.append((nr, nc))
                        grid[nr][nc] = 0

            return total

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    total = bfs(i, j)
                    if total % k == 0:
                        count += 1

        return count
