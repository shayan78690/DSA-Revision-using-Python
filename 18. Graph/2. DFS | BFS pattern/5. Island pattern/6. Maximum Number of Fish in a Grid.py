class Solution(object):
    def findMaxFish(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
                return 0

            fish = grid[i][j]
            grid[i][j] = 0

            fish += dfs(i + 1, j)
            fish += dfs(i - 1, j)
            fish += dfs(i, j + 1)
            fish += dfs(i, j - 1)

            return fish

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, dfs(i, j))

        return ans



from collections import deque

class Solution(object):
    def findMaxFish(self, grid):
        n, m = len(grid), len(grid[0])

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr, sc):
            q = deque()
            q.append((sr, sc))

            fish = grid[sr][sc]
            grid[sr][sc] = 0

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0:
                        fish += grid[nr][nc]
                        grid[nr][nc] = 0
                        q.append((nr, nc))

            return fish

        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans, bfs(i, j))

        return ans
