class Solution:
    def countStrings(self, n):
        dp = [[-1] * 2 for _ in range(n)]
        return self.func(n, 0, False, dp)

    def func(self, n, idx, prevOne, dp):
        if idx == n:
            return 1
        if dp[idx][prevOne] != -1:
            return dp[idx][prevOne]
        count = 0
        count += self.func(n, idx + 1, False, dp)

        if not prevOne:
            count += self.func(n, idx + 1, True, dp)
        
        dp[idx][prevOne] = count
        return dp[idx][prevOne]


class Solution:
    def countStrings(self, n):
        dp = [[0] * 2 for _ in range(n + 1)]

        dp[n][0] = dp[n][1] = 1

        for i in range(n - 1, -1, -1):
            dp[i][0] = dp[i + 1][0] + dp[i + 1][1]
            dp[i][1] = dp[i + 1][0]

        return dp[0][0]
