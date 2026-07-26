class Solution(object):

    def dfs(self, grid, n, m, i, j):
        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] == 0:
            return
        grid[i][j] = 0
        self.dfs(grid, n, m, i+1, j)
        self.dfs(grid, n, m, i-1, j)
        self.dfs(grid, n, m, i, j+1)
        self.dfs(grid, n, m, i, j-1)

    def numEnclaves(self, grid):
        n, m = len(grid), len(grid[0])
        for i in range(n):
            if grid[i][0] == 1:
                self.dfs(grid, n, m, i, 0)
            if grid[i][m-1] == 1:
                self.dfs(grid, n, m, i, m-1)
        
        for j in range(m):
            if grid[0][j] == 1:
                self.dfs(grid, n, m, 0, j)
            if grid[n-1][j] == 1:
                self.dfs(grid, n, m, n-1, j)
        
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count
        





from collections import deque
class Solution(object):

    def add(self, grid, i, j, q):
        grid[i][j] = 0
        q.append((i, j))

    def numEnclaves(self, grid):
        n, m = len(grid), len(grid[0])
        q = deque()

        for i in range(n):
            if grid[i][0] == 1:
                self.add(grid, i, 0, q)
            if grid[i][m-1] == 1:
                self.add(grid, i, m-1, q)
        
        for j in range(m):
            if grid[0][j] == 1:
                self.add(grid, 0, j, q)
            if grid[n-1][j] == 1:
                self.add(grid, n-1, j, q)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    self.add(grid, nr, nc, q)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count
        



