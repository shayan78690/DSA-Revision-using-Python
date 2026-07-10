class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        return self.func(str1, str2, 0, 0)
    def func(self, s1, s2, i, j):
        if i == len(s1):
            return s2[j:]

        if j == len(s2):
            return s1[i:]

        if s1[i] == s2[j]:
            return s1[i] + self.func(s1, s2, i + 1, j + 1)

        first = s1[i] + self.func(s1, s2, i + 1, j)
        second = s2[j] + self.func(s1, s2, i, j + 1)

        if len(first) < len(second):
            return first

        return second



class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        n = len(str1)
        m = len(str2)

        dp = [[None] * (m + 1) for _ in range(n + 1)]

        return self.func(str1, str2, 0, 0, dp)

    def func(self, s1, s2, i, j, dp):

        if i == len(s1):
            return s2[j:]

        if j == len(s2):
            return s1[i:]

        if dp[i][j] is not None:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = s1[i] + self.func(s1, s2, i + 1, j + 1, dp)
            return dp[i][j]

        first = s1[i] + self.func(s1, s2, i + 1, j, dp)
        second = s2[j] + self.func(s1, s2, i, j + 1, dp)

        if len(first) < len(second):
            dp[i][j] = first
        else:
            dp[i][j] = second

        return dp[i][j]


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
