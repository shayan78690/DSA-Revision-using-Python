class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n, m = len(text1), len(text2)
        return self.func(text1, text2, n, m, 0, 0)
    
    def func(self, text1, text2, n, m, i, j):
        if i == n or j == m:
            return 0
        if text1[i] == text2[j]:
            return 1 + self.func(text1, text2, n, m, i+1, j+1)
        skip1 = self.func(text1, text2, n, m, i+1, j)
        skip2 = self.func(text1, text2, n, m, i, j+1)
        return max(skip1, skip2)



class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[-1] * m for _ in range(n)]
        return self.func(text1, text2, 0, 0, dp)
    def func(self, s1, s2, i, j, dp):
        if i == len(s1) or j == len(s2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.func(s1, s2, i + 1, j + 1, dp)
        else:
            skip1 = self.func(s1, s2, i+1, j, dp)
            skip2 = self.func(s1, s2, i, j+1, dp)
            dp[i][j] = max(skip1, skip2)
        return dp[i][j]


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    skip1 = dp[i+1][j]
                    skip2 = dp[i][j+1]
                    dp[i][j] = max(skip1, skip2)
        return dp[0][0]
