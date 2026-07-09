class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        return self.func(obstacleGrid, n, m, 0, 0)

    def func(self, grid, n, m, i, j):
        if i >= n or j >= m:
            return 0

        if grid[i][j] == 1:
            return 0

        if i == n-1 and j == m-1:
            return 1

        right = self.func(grid, n, m, i, j+1)
        down = self.func(grid, n, m, i+1, j)

        return right + down



class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1] * m for _ in range(n)]
        return self.func(obstacleGrid, n, m, 0, 0, dp)

    def func(self, grid, n, m, i, j, dp):
        if i >= n or j >= m:
            return 0
        if grid[i][j] == 1:
            return 0
        if i == n-1 and j == m-1:
            return 1
        if dp[i][j] != -1:
            return dp[i][j]
        right = self.func(grid, n, m, i, j+1, dp)
        down = self.func(grid, n, m, i+1, j, dp)
        dp[i][j] = right+down   
        return dp[i][j]


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == n-1 and j == m-1:
                    dp[i][j] = 1
                else:
                    right = 0
                    down = 0
                    if j+1 < m:
                        right = dp[i][j+1]
                    if i+1 < n:
                        down = dp[i+1][j]
                    dp[i][j] = right+down
        return dp[0][0]

    
