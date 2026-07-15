class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[-1] * n for _ in range(n)]
        return self.func(arr, 1, n-1, dp)
        
    def func(self, arr, i, j, dp):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = float('inf')
        for k in range(i, j):
            cost = (self.func(arr, i, k, dp) + self.func(arr, k+1, j, dp) + arr[i-1] * arr[k] * arr[j])
            ans = min(ans, cost)
        dp[i][j] = ans
        return dp[i][j]



class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, 0, -1):
            for j in range(i+1, n):
                mini = float('inf')
                for k in range(i, j):
                    cost = (arr[i-1]*arr[k]*arr[j]) + dp[i][k] + dp[k+1][j]
                    mini = min(mini, cost)
                dp[i][j] = mini
        return dp[1][n-1]
        
        



