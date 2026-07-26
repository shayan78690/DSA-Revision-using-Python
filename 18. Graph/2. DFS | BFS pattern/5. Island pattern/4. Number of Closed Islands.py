class Solution(object):
    def closedIsland(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0  or j >= m or grid[i][j] == 1:
                return
            grid[i][j] = 1
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        for i in range(n):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][m-1] == 0:
                dfs(i, m-1)
        
        for j in range(m):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[n-1][j] == 0:
                dfs(n-1, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count        




from collections import deque

class Solution(object):
    def closedIsland(self, grid):
        n, m = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(sr, sc):
            q = deque()
            q.append((sr, sc))
            grid[sr][sc] = 1

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr, nc))

        # Remove boundary-connected land
        for i in range(n):
            if grid[i][0] == 0:
                bfs(i, 0)
            if grid[i][m - 1] == 0:
                bfs(i, m - 1)

        for j in range(m):
            if grid[0][j] == 0:
                bfs(0, j)
            if grid[n - 1][j] == 0:
                bfs(n - 1, j)

        # Count remaining closed islands
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    bfs(i, j)
                    count += 1

        return count
