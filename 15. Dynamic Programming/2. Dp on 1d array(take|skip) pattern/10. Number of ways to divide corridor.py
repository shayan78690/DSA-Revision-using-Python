class Solution(object):
    def numberOfWays(self, corridor):
        n = len(corridor)
        MOD = 10**9+7
        dp = [[-1] * 3 for _ in range(n)]
        return self.solve(corridor, n, 0, 0, MOD, dp)
    
    def solve(self, corridor, n, index, seats, MOD, dp):
        if index == n:
            if seats == 2:
                return 1
            return 0
        if dp[index][seats] != -1:
            return dp[index][seats]
        count = 0
        if corridor[index] == "S":
            if seats < 2:
                count = (count + self.solve(corridor, n, index+1, seats+1, MOD, dp)) % MOD
            else:
                count = (count + self.solve(corridor, n, index+1, 1, MOD, dp)) % MOD
        else:
            count = (count + self.solve(corridor, n, index+1, seats, MOD, dp)) % MOD
            if seats == 2:
                count = (count + self.solve(corridor, n, index+1, 0, MOD, dp)) % MOD
        dp[index][seats] = count
        return count




class Solution(object):
    def numberOfWays(self, corridor):
        n = len(corridor)
        MOD = 10**9+7
        dp = [[0] * 3 for _ in range(n+1)]
        dp[n][2] = 1
        for index in range(n-1, -1, -1):
            for seats in range(3):
                count = 0
                if corridor[index] == "S":
                    if seats < 2:
                        count = (count + dp[index+1][seats+1]) % MOD
                    else:
                        count = (count + dp[index+1][1]) % MOD
                else:
                    count = (count + dp[index+1][seats]) % MOD
                    if seats == 2:
                        count = (count + dp[index+1][0]) % MOD
                dp[index][seats] = count
        return dp[0][0]
    


        


