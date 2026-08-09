class Solution(object):
    def waysToReachTarget(self, target, types):
        n = len(types)
        MOD = 10**9+7
        return self.solve(types, n, 0, target, MOD)
    
    def solve(self, types, n, index, target, MOD):
        if target == 0:
            return 1
        if index == n:
            return 0
        count, marks = types[index]
        ways = 0
        for take in range(count+1):
            points = take * marks
            if points > target:
                break
            ways = (ways + self.solve(types, n, index+1, target-points, MOD)) % MOD
        return ways


class Solution(object):
    def waysToReachTarget(self, target, types):
        n = len(types)
        MOD = 10**9+7
        dp = [[-1] * (target+1) for _ in range(n+1)]
        return self.solve(types, n, 0, target, MOD, dp)
    
    def solve(self, types, n, index, target, MOD, dp):
        if target == 0:
            return 1
        if index == n:
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        count, marks = types[index]
        ways = 0
        for take in range(count+1):
            points = take * marks
            if points > target:
                break
            ways = (ways + self.solve(types, n, index+1, target-points, MOD, dp)) % MOD
        dp[index][target] = ways
        return ways


class Solution(object):
    def waysToReachTarget(self, target, types):
        n = len(types)
        MOD = 10**9+7
        dp = [[0] * (target+1) for _ in range(n+1)]
        for index in range(n+1):
            dp[index][0] = 1
        for index in range(n-1, -1, -1):
            for target in range(1, target+1):
                count, marks = types[index]
                ways = 0
                for take in range(count+1):
                    points = take * marks
                    if points > target:
                        break
                    ways = (ways + dp[index+1][target-points]) % MOD
                dp[index][target] = ways
        return dp[0][target] 

