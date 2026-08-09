class Solution:
    def maximumPath(self, mat):
        n, m = len(mat), len(mat[0])
        maxi = float('-inf')
        dp = [[-1] * m for _ in range(n)] 
        for j in range(m):
            maxi = max(maxi, self.func(mat, n, m, 0, j, dp))
        return maxi
        
    def func(self, mat, n, m, i, j, dp):
        if j < 0 or j >= m:
            return float('-inf')
        if i == n-1:
            return mat[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        left = mat[i][j] + self.func(mat, n, m, i+1, j-1, dp)
        down = mat[i][j] + self.func(mat, n, m, i+1, j, dp)
        right = mat[i][j] + self.func(mat, n, m, i+1, j+1, dp)
        dp[i][j] = max(left, down, right)
        return dp[i][j]


class Solution:
    def maximumPath(self, mat):
        n, m = len(mat), len(mat[0])
        maxi = float('-inf')
        dp = [[0] * m for _ in range(n)] 
        for j in range(m):
            dp[n-1][j] = mat[n-1][j]
        
        for i in range(n-2, -1, -1):
            for j in range(m):
                down = mat[i][j] + dp[i+1][j]
                right = float('-inf')
                left = float('-inf')
                if j > 0:
                    left = mat[i][j] + dp[i+1][j-1]
                if j < m-1:
                    right = mat[i][j] + dp[i+1][j+1]
                dp[i][j] = max(left, right, down)
        return max(dp[0])
        
