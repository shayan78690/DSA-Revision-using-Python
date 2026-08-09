class Solution:
    def countStrings(self, n):
        dp = [[-1] * 2 for _ in range(n)]
        return self.func(n, 0, 0, dp)

    def func(self, n, idx, prev, dp):
        if idx == n:
            return 1
        if dp[idx][prev] != -1:
            return dp[idx][prev]
        count = 0
        count += self.func(n, idx + 1, 0, dp)

        if prev == 0:
            count += self.func(n, idx + 1, 1, dp)
        
        dp[idx][prev] = count
        return dp[idx][prev]


class Solution:
    def countStrings(self, n):
        dp = [[0] * 2 for _ in range(n+1)]
        dp[n][0] = 1
        dp[n][1] = 1
        for idx in range(n-1, -1, -1):
            for prev in range(2):
                count = 0
                count += dp[idx+1][0]
                if prev == 0:
                    count += dp[idx+1][1]
                dp[idx][prev] = count
        return dp[0][0]

   
