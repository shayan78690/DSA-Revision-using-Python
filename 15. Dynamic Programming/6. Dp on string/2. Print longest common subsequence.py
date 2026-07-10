class Solution:
    def longestCommonSubsequence(self, text1, text2):
        return self.func(text1, text2, 0, 0)

    def func(self, s1, s2, i, j):
        if i == len(s1) or j == len(s2):
            return ""

        if s1[i] == s2[j]:
            return s1[i] + self.func(s1, s2, i + 1, j + 1)

        skip1 = self.func(s1, s2, i + 1, j)
        skip2 = self.func(s1, s2, i, j + 1)

        if len(skip1) > len(skip2):
            return skip1
        else:
            return skip2


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[None] * m for _ in range(n)]

        return self.func(text1, text2, 0, 0, dp)

    def func(self, s1, s2, i, j, dp):
        if i == len(s1) or j == len(s2):
            return ""

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = s1[i] + self.func(s1, s2, i + 1, j + 1, dp)
        else:
            skip1 = self.func(s1, s2, i + 1, j, dp)
            skip2 = self.func(s1, s2, i, j + 1, dp)

            if len(skip1) > len(skip2):
                dp[i][j] = skip1
            else:
                dp[i][j] = skip2

        return dp[i][j]


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[""] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = text1[i] + dp[i + 1][j + 1]
                else:
                    if len(dp[i + 1][j]) > len(dp[i][j + 1]):
                        dp[i][j] = dp[i + 1][j]
                    else:
                        dp[i][j] = dp[i][j + 1]

        return dp[0][0]





class Solution:
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        ans = []

        i = 0
        j = 0

        while i < n and j < m:

            if text1[i] == text2[j]:
                ans.append(text1[i])
                i += 1
                j += 1

            elif dp[i + 1][j] >= dp[i][j + 1]:
                i += 1

            else:
                j += 1

        return "".join(ans)
