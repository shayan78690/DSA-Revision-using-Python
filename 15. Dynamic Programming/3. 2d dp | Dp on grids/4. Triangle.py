class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        return self.func(triangle, n, 0, 0)
    
    def func(self, triangle, n, i, j):
        if i == n-1:
            return triangle[i][j]
        down = triangle[i][j] + self.func(triangle, n, i+1, j)
        diagonal = triangle[i][j] + self.func(triangle, n, i+1, j+1)
        return min(down, diagonal)



class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[-1] * n for _ in range(n)]
        return self.func(triangle, n, 0, 0, dp)
    
    def func(self, triangle, n, i, j, dp):
        if i == n-1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + self.func(triangle, n, i+1, j, dp)
        diagonal = triangle[i][j] + self.func(triangle, n, i+1, j+1, dp)
        dp[i][j] = min(down, diagonal)
        return dp[i][j]
        class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(i+1):
                down = triangle[i][j] + dp[i+1][j]
                diagonal = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, diagonal)
        return dp[0][0]
    
 
        
