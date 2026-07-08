class Solution(object):
    def minCostClimbingStairs(self, cost):
        return min(self.func(cost, 0), self.func(cost, 1))
    
    def func(self, cost, index):
        if index >= len(cost):
            return 0
        onestep = cost[index] + self.func(cost, index+1)
        twostep = cost[index] + self.func(cost, index+2)
        return min(onestep, twostep)


class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [-1] * len(cost)
        return min(self.func(cost, 0, dp), self.func(cost, 1, dp))
    
    def func(self, cost, index, dp):
        if index >= len(cost):
            return 0
        if dp[index] != -1:
            return dp[index]
        onestep = cost[index] + self.func(cost, index+1, dp)
        twostep = cost[index] + self.func(cost, index+2, dp)
        dp[index] = min(onestep, twostep)
        return dp[index]

  class Solution(object):
    def minCostClimbingStairs(self, cost):
        dp = [-1] * len(cost)
        n = len(cost)
        return min(self.func(cost, n-1, dp), self.func(cost, n-2, dp))
    
    def func(self, cost, index, dp):
        if index < 0:
            return 0
        if dp[index] != -1:
            return dp[index]
        onestep = cost[index] + self.func(cost, index-1, dp)
        twostep = cost[index] + self.func(cost, index-2, dp)
        dp[index] = min(onestep, twostep)
        return dp[index]


class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        return min(dp[0], dp[1])
    

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[n-1], dp[n-2])        
