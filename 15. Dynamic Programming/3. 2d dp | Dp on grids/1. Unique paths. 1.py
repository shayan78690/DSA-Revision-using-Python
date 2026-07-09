class Solution(object):
    def uniquePaths(self, m, n):
        return self.func(m, n, 0, 0)
    
    def func(self, m, n, i, j):
        if i == m-1 and j == n-1:
            return 1
        if i >= m or j >= n:
            return 0
        right = self.func(m, n, i, j+1)
        down = self.func(m, n, i+1, j)
        return right + down


class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[-1] * n for _ in range(m)]
        return self.func(m, n, 0, 0, dp)
    
    def func(self, m, n, i, j, dp):
        if i == m-1 and j == n-1:
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        right = self.func(m, n, i, j+1, dp)
        down = self.func(m, n, i+1, j, dp)
        dp[i][j] = right + down
        return dp[i][j]


class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                right = 0
                down = 0
                if j+1 < n:
                    right = dp[i][j+1]
                if i+1 < m:
                    down = dp[i+1][j]
                dp[i][j] = right+down
        return dp[0][0]
    

        
