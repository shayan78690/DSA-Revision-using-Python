class Solution(object):
    def numSquares(self, n):
        return self.func(n)

    def func(self, n):
        if n == 0:
            return 0
        ans = float('inf')
        i = 1
        while i*i <= n:
            ans = min(ans, 1 + self.func(n-i*i))
            i += 1
        return ans

  class Solution(object):
    def numSquares(self, n):
        dp = [-1] * (n+1)
        return self.func(n, dp)

    def func(self, n, dp):
        if n == 0:
            return 0
        if dp[n] != -1:
            return dp[n]
        ans = float('inf')
        i = 1
        while i*i <= n:
            ans = min(ans, 1 + self.func(n-i*i, dp))
            i += 1
        dp[n] = ans
        return dp[n]


