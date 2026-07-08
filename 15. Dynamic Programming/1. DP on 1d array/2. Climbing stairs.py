if n <= 1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)

class Solution(object):
    def climbStairs(self, n):
        dp = [-1] * (n+1)
        return self.func(n, dp)
    def func(self, n, dp):
        if n <= 1:
            return 1
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.func(n-1, dp)+self.func(n-2, dp)
        return dp[n]

class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        dp = [-1] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    
        
