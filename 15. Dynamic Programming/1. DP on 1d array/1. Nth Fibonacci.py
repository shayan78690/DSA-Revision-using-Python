class Solution(object):
    def fib(self, n):
        dp = [-1] * (n+1)
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        
class Solution(object):
    def fib(self, n):
        dp = [-1] * (n+1)
        return self.func(n, dp)
    
    def func(self, n, dp):
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.func(n-1, dp) + self.func(n-2, dp)
        return dp[n]
    
class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        dp = [-1] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
