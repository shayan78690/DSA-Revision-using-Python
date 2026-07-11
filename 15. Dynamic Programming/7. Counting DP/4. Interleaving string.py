class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        return self.func(s1, s2, s3, 0, 0)

    def func(self, s1, s2, s3, i, j):

        if i == len(s1) and j == len(s2):
            return True

        k = i + j

        # Condition 1 : Both match
        if (i < len(s1) and j < len(s2) and
            s1[i] == s3[k] and s2[j] == s3[k]):
            return (self.func(s1, s2, s3, i + 1, j) or
                    self.func(s1, s2, s3, i, j + 1))

        # Condition 2 : Only s1 matches
        if i < len(s1) and s1[i] == s3[k]:
            return self.func(s1, s2, s3, i + 1, j)

        # Condition 3 : Only s2 matches
        if j < len(s2) and s2[j] == s3[k]:
            return self.func(s1, s2, s3, i, j + 1)

        return False


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        n, m = len(s1), len(s2)
        dp = [[None] * m for _ in range(n)]
        return self.func(s1, s2, s3, 0, 0, dp)

    def func(self, s1, s2, s3, i, j, dp):

        if i == len(s1) and j == len(s2):
            return True
        if dp[i][j] is not None:
            return dp[i][j]

        k = i + j

        # Condition 1 : Both match
        if (i < len(s1) and j < len(s2) and
            s1[i] == s3[k] and s2[j] == s3[k]):
            dp[i][j] = (self.func(s1, s2, s3, i + 1, j, dp) or
                    self.func(s1, s2, s3, i, j + 1, dp))

        # Condition 2 : Only s1 matches
        if i < len(s1) and s1[i] == s3[k]:
            dp[i][j] = self.func(s1, s2, s3, i + 1, j, dp)

        # Condition 3 : Only s2 matches
        if j < len(s2) and s2[j] == s3[k]:
            dp[i][j] = self.func(s1, s2, s3, i, j + 1, dp)

        return dp[i][j]


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        n, m = len(s1), len(s2)
        dp = [[None] * (m+1) for _ in range(n+1)]
        return self.func(s1, s2, s3, 0, 0, dp)

    def func(self, s1, s2, s3, i, j, dp):

        if i == len(s1) and j == len(s2):
            return True
        if dp[i][j] is not None:
            return dp[i][j]

        k = i + j

        # Condition 1 : Both match
        if (i < len(s1) and j < len(s2) and
            s1[i] == s3[k] and s2[j] == s3[k]):
            dp[i][j] = (self.func(s1, s2, s3, i + 1, j, dp) or
                    self.func(s1, s2, s3, i, j + 1, dp))

        # Condition 2 : Only s1 matches
        if i < len(s1) and s1[i] == s3[k]:
            dp[i][j] = self.func(s1, s2, s3, i + 1, j, dp)

        # Condition 3 : Only s2 matches
        if j < len(s2) and s2[j] == s3[k]:
            dp[i][j] = self.func(s1, s2, s3, i, j + 1, dp)

        return dp[i][j]

  class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        
        # n, m = len(s1), len(s2)
        # dp = [[None] * (m+1) for _ in range(n+1)]
        return self.func(s1, s2, s3, 0, 0)

    def func(self, s1, s2, s3, i, j):
        if i == len(s1) and j == len(s2):
            return True
        
        k = i+j
        if i < len(s1) and s1[i] == s3[k]:
            if self.func(s1, s2, s3, i+1, j):
                return True
        
        if j < len(s2) and s2[j] == s3[k]:
            if self.func(s1, s2, s3, i, j+1):
                return True
        
        return False



class Solution(object):
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False

        n, m = len(s1), len(s2)
        dp = [[None] * (m + 1) for _ in range(n + 1)]

        return self.func(s1, s2, s3, 0, 0, dp)

    def func(self, s1, s2, s3, i, j, dp):

        if i == len(s1) and j == len(s2):
            return True

        if dp[i][j] is not None:
            return dp[i][j]

        k = i + j

        if i < len(s1) and s1[i] == s3[k]:
            if self.func(s1, s2, s3, i + 1, j, dp):
                dp[i][j] = True
                return True

        if j < len(s2) and s2[j] == s3[k]:
            if self.func(s1, s2, s3, i, j + 1, dp):
                dp[i][j] = True
                return True

        dp[i][j] = False
        return False


