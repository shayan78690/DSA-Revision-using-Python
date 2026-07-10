class Solution:
	def minOperations(self, s1, s2):
		lcs = self.func(s1, s2, 0, 0)
		deletion = len(s1)-lcs
		insertion = len(s2)-lcs
		return insertion+deletion
	
	def func(self, s1, s2, i, j):
	    if i == len(s1) or j == len(s2):
	        return 0
	    if s1[i] == s2[j]:
	        return 1 + self.func(s1, s2, i+1, j+1)
	    skip1 = self.func(s1, s2, i+1, j)
	    skip2 = self.func(s1, s2, i, j+1)
	    return max(skip1, skip2)


class Solution:
    def minOperations(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[-1] * m for _ in range(n)]

        lcs = self.func(s1, s2, 0, 0, dp)

        deletion = n - lcs
        insertion = m - lcs

        return deletion + insertion

    def func(self, s1, s2, i, j, dp):

        if i == len(s1) or j == len(s2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 1 + self.func(s1, s2, i + 1, j + 1, dp)
        else:
            skip1 = self.func(s1, s2, i + 1, j, dp)
            skip2 = self.func(s1, s2, i, j + 1, dp)

            dp[i][j] = max(skip1, skip2)

        return dp[i][j]


class Solution:
    def minOperations(self, s1, s2):
        n = len(s1)
        m = len(s2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if s1[i] == s2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )

        lcs = dp[0][0]

        deletion = n - lcs
        insertion = m - lcs

        return deletion + insertion
