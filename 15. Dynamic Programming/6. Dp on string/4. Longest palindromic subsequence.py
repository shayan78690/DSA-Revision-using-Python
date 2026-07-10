class Solution:
    def longestPalindromeSubseq(self, s):
        rev = s[::-1]
        return self.func(s, rev, 0, 0)

    def func(self, s, rev, i, j):

        if i == len(s) or j == len(rev):
            return 0

        if s[i] == rev[j]:
            return 1 + self.func(s, rev, i + 1, j + 1)

        return max(
            self.func(s, rev, i + 1, j),
            self.func(s, rev, i, j + 1)
        )



class Solution:
    def longestPalindromeSubseq(self, s):
        rev = s[::-1]

        n = len(s)
        m = len(rev)

        dp = [[-1] * m for _ in range(n)]

        return self.func(s, rev, 0, 0, dp)

    def func(self, s, rev, i, j, dp):

        if i == len(s) or j == len(rev):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == rev[j]:
            dp[i][j] = 1 + self.func(s, rev, i + 1, j + 1, dp)
        else:
            dp[i][j] = max(
                self.func(s, rev, i + 1, j, dp),
                self.func(s, rev, i, j + 1, dp)
            )

        return dp[i][j]


class Solution:
    def longestPalindromeSubseq(self, s):
        rev = s[::-1]

        n = len(s)
        m = len(rev)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if s[i] == rev[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        return dp[0][0]
