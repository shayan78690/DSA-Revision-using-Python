class Solution:
    def minSuperSeq(self, s1, s2):
        n, m = len(s1), len(s2)
        lcs = self.func(s1, s2, n, m, 0, 0)
        return (n+m)-lcs
    
    def func(self, s1, s2, n, m, i, j):
        if i == n or j == m:
            return 0
        if s1[i] == s2[j]:
            return 1 + self.func(s1, s2, n, m, i+1, j+1)
        skip1 = self.func(s1, s2, n, m, i+1, j)
        skip2 = self.func(s1, s2, n, m, i, j+1)
        return max(skip1, skip2)

class Solution:
    def minSuperSeq(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[-1] * m for _ in range(n)]
        lcs = self.func(s1, s2, n, m, 0, 0, dp)
        return (n+m)-lcs
    
    def func(self, s1, s2, n, m, i, j, dp):
        if i == n or j == m:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.func(s1, s2, n, m, i+1, j+1, dp)
        else:
            skip1 = self.func(s1, s2, n, m, i+1, j, dp)
            skip2 = self.func(s1, s2, n, m, i, j+1, dp)
            dp[i][j] = max(skip1, skip2)
        return dp[i][j]


class Solution:
    def minSuperSeq(self, s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        lcs = dp[0][0]
        return (n+m)-lcs
    





class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):

        n = len(str1)
        m = len(str2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if str1[i] == str2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        i = 0
        j = 0
        ans = []

        while i < n and j < m:

            if str1[i] == str2[j]:
                ans.append(str1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] > dp[i][j + 1]:
                ans.append(str1[i])
                i += 1

            else:
                ans.append(str2[j])
                j += 1

        while i < n:
            ans.append(str1[i])
            i += 1

        while j < m:
            ans.append(str2[j])
            j += 1

        return "".join(ans)
