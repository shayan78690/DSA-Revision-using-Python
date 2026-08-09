class Solution(object):
    def countHousePlacements(self, n):
        ways = self.func(n, 0, 0)
        return ways * ways
    def func(self, n, index, prev):
        if index == n:
            return 1
        skip = self.func(n, index+1, 0)
        take = 0
        if prev == 0:
            take = self.func(n, index+1, 1)
        return take+skip

class Solution(object):
    def countHousePlacements(self, n):
        MOD = 10**9 + 7
        dp = [[-1] * 2 for _ in range(n + 1)]
        ways = self.func(n, 0, 0, dp, MOD)
        return (ways * ways) % MOD

    def func(self, n, index, prev, dp, MOD):
        if index == n:
            return 1
        if dp[index][prev] != -1:
            return dp[index][prev]
        count = 0
        count += self.func(n, index + 1, 0, dp, MOD)
        if prev == 0:
            count += self.func(n, index + 1, 1, dp, MOD)
        dp[index][prev] = count % MOD
        return dp[index][prev]


class Solution(object):
    def countHousePlacements(self, n):
        MOD = 10**9 + 7
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][0] = 1
        dp[n][1] = 1
        for index in range(n-1, -1, -1):
            for prev in range(2):
                count = 0
                count += dp[index+1][0]
                if prev == 0:
                    count += dp[index+1][1]
                dp[index][prev] = count % MOD
        return (dp[0][0] * dp[0][0]) % MOD







