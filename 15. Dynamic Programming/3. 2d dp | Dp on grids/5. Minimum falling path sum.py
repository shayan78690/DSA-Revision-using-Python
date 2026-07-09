class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        mini = float('inf')
        for j in range(n):
            mini = min(mini, self.func(matrix, n, 0, j))
        return mini
    
    def func(self, matrix, n, i, j):
        if j < 0 or j >= n:
            return float('inf')
        if i == n-1:
            return matrix[i][j]
        leftDiagonal = matrix[i][j] + self.func(matrix, n, i+1, j-1)
        down = matrix[i][j] + self.func(matrix, n, i+1, j)
        rightDiagonal = matrix[i][j] + self.func(matrix, n, i+1, j+1)
        return min(leftDiagonal, down, rightDiagonal)


class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        mini = float('inf')
        dp = [[-1] * n for _ in range(n)]
        for j in range(n):
            mini = min(mini, self.func(matrix, n, 0, j, dp))
        return mini
    
    def func(self, matrix, n, i, j, dp):
        if j < 0 or j >= n:
            return float('inf')
        if i == n-1:
            return matrix[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        leftDiagonal = matrix[i][j] + self.func(matrix, n, i+1, j-1, dp)
        down = matrix[i][j] + self.func(matrix, n, i+1, j, dp)
        rightDiagonal = matrix[i][j] + self.func(matrix, n, i+1, j+1, dp)
        dp[i][j] = min(leftDiagonal, down, rightDiagonal)
        return dp[i][j]


class Solution(object):
    def minFallingPathSum(self, matrix):
        n = len(matrix)
        mini = float('inf')
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]

        for i in range(n-2, -1, -1):
            for j in range(n):
                down = matrix[i][j] + dp[i+1][j]
                leftDiagonal = float('inf')
                rightDiagonal = float('inf')
                if j > 0:
                    leftDiagonal = matrix[i][j] + dp[i+1][j-1]
                if j < n-1:
                    rightDiagonal = matrix[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, leftDiagonal, rightDiagonal)
        return min(dp[0])
