class Solution(object):
    def numDistinct(self, s, t):
        return self.func(s, t, 0, 0)
    
    def func(self, s, t, i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if s[i] == t[j]:
            take = self.func(s, t, i+1, j+1)
            skip = self.func(s, t, i+1, j)
            return take + skip
        else:
            return self.func(s, t, i+1, j)


class Solution(object):
    def numDistinct(self, s, t):
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][m] = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        return dp[0][0]
    
