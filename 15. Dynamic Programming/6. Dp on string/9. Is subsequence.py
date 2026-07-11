class Solution(object):
    def isSubsequence(self, s, t):
        n, m = len(s), len(t)
        dp = [[None] * m for _ in range(n)]
        return self.func(s, t, 0, 0, dp)
    
    def func(self, s, t, i, j, dp):
        if i == len(s):
            return True
        if j == len(t):
            return False
        if dp[i][j] is not None:
            return dp[i][j]
        if s[i] == t[j]:
            dp[i][j] = self.func(s, t, i+1, j+1, dp)
        else:
            dp[i][j] = self.func(s, t, i, j+1, dp)
        return dp[i][j]


class Solution(object):
    def isSubsequence(self, s, t):
        n, m = len(s), len(t)
        dp = [[False] * (m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[n][j] = True
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]
    



class Solution(object):
    def isSubsequence(self, s, t):
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        
        return i == len(s)
