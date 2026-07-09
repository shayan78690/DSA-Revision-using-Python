class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        return self.func(grid, n, m, 0, 0)
    
    def func(self, grid, n, m, i, j):
        if i == n-1 and j == m-1:
            return grid[i][j]
        if i >= n or j >= m:
            return float('inf')
        right = grid[i][j] + self.func(grid, n, m, i, j+1)
        down = grid[i][j] + self.func(grid, n, m, i+1, j)
        return min(right, down)


class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[-1] * m for _ in range(n)]
        return self.func(grid, n, m, 0, 0, dp)
    
    def func(self, grid, n, m, i, j, dp):
        if i == n-1 and j == m-1:
            return grid[i][j]
        if i >= n or j >= m:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        
        right = grid[i][j] + self.func(grid, n, m, i, j+1, dp)
        down = grid[i][j] + self.func(grid, n, m, i+1, j, dp)
        dp[i][j] = min(right, down)
        return dp[i][j]



class Solution(object):
    def minPathSum(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    dp[i][j] = grid[i][j]
                else:
                    right = float('inf')
                    down = float('inf')
                    if j+1 < m:
                        right = grid[i][j] + dp[i][j+1]
                    if i+1< n:
                        down = grid[i][j] + dp[i+1][j]
                    dp[i][j] = min(right, down)
        return dp[0][0]
