class Solution(object):
    def numberOfWays(self, n, x):
        mod = 10**9+7
        return self.func(n, x, 1) % mod
        
    def func(self, n, x, number):
        if n == 0:
            return 1
        if number**x > n:
            return 0
        take = self.func(n-number**x, x, number+1)
        skip = self.func(n, x, number+1)
        return take+skip
        

class Solution(object):
    def numberOfWays(self, n, x):
        mod = 10**9+7
        dp = [[-1] * (n+2) for _ in range(n+1)]
        return self.func(n, x, 1, dp) % mod
        
    def func(self, n, x, number, dp):
        if n == 0:
            return 1
        if number**x > n:
            return 0
        if dp[n][number] != -1:
            return dp[n][number]
        take = self.func(n-number**x, x, number+1, dp)
        skip = self.func(n, x, number+1, dp)
        dp[n][number] = take+skip
        return dp[n][number]



class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9+7
        dp = [[-1] * (n+1) for _ in range(n+1)]
        return self.solve(n, x, 1, dp, MOD)
    
    def solve(self, n, x, number, dp, MOD):
        if n == 0:
            return 1
        power = number**x
        if power > n:
            return 0
        if dp[n][number] != -1:
            return dp[n][number]
        count = 0
        count = (count + self.solve(n-power, x, number+1, dp, MOD)) % MOD
        count = (count + self.solve(n, x, number+1, dp, MOD)) % MOD
        dp[n][number] = count
        return dp[n][number]



class Solution(object):
    def numberOfWays(self, n, x):
        MOD = 10**9+7
        dp = [[0] * (n+2) for _ in range(n+1)]
        for number in range(n+2):
            dp[0][number] = 1
        for remaining in range(1, n+1):
            for number in range(n, 0, -1):
                power = number**x
                if power > remaining:
                    dp[remaining][number] = 0
                    continue
                count = 0
                count = (count + dp[remaining-power][number+1]) % MOD
                count = (count + dp[remaining][number+1]) % MOD

                dp[remaining][number] = count
        return dp[n][1] 
