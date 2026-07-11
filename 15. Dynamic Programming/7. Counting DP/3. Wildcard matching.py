class Solution(object):
    def isMatch(self, s, p):
        return self.func(s, p, 0, 0)
    
    def func(self, s, p, i, j):
        if i == n and j == m:
          return True
        # pattern finished
        if j == len(p):
            return False
        # string finished
        if i == len(s):
            while j < len(p):
                if p[j] != "*":
                    return False
                j += 1
            return True
        # character matched
        if s[i] == p[j] or p[j] == "?":
            return self.func(s, p, i+1, j+1)
        
        # if contains "*"
        if p[j] == "*":
            return self.func(s, p, i+1, j) or self.func(s, p, i, j+1)
        
        if s[i] != p[j]:
            return False



class Solution(object):
    def isMatch(self, s, p):
        n, m = len(s), len(p)
        dp = [[None] * (m + 1) for _ in range(n + 1)]
        return self.func(s, p, 0, 0, dp)

    def func(self, s, p, i, j, dp):

        if i == len(s) and j == len(p):
            return True

        if j == len(p):
            return False

        if i == len(s):
            while j < len(p):
                if p[j] != '*':
                    return False
                j += 1
            return True

        if dp[i][j] is not None:
            return dp[i][j]

        if s[i] == p[j] or p[j] == '?':
            dp[i][j] = self.func(s, p, i + 1, j + 1, dp)

        elif p[j] == '*':
            dp[i][j] = (
                self.func(s, p, i + 1, j, dp) or
                self.func(s, p, i, j + 1, dp)
            )

        else:
            dp[i][j] = False

        return dp[i][j]

class Solution(object):
    def isMatch(self, s, p):
        n, m = len(s), len(p)

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[n][m] = True
        for j in range(m, -1, -1):
            k = j
            while k < m:
                if p[k] != '*':
                    dp[n][j] = False
                    break
                k += 1
            else:
                dp[n][j] = True

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i + 1][j + 1]

                elif p[j] == '*':
                    dp[i][j] = dp[i + 1][j] or dp[i][j + 1]

        return dp[0][0]
