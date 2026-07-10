class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        return self.func(W, val, wt, 0, n)

    def func(self, W, val, wt, index, n):
        if index == n or W == 0:
            return 0

        exclude = self.func(W, val, wt, index + 1, n)

        include = 0
        if wt[index] <= W:
            include = val[index] + self.func(W - wt[index], val, wt, index + 1, n)

        return max(include, exclude)


class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[-1] * (W+1) for _ in range(n)]
        return self.func(W, val, wt, 0, n, dp)
    
    def func(self, W, val, wt, index, n, dp):
        if index == n or W == 0:
            return 0
        
        if dp[index][W] != -1:
            return dp[index][W]
        
        exclude = self.func(W, val, wt, index+1, n, dp)
        
        include = 0
        if wt[index] <= W:
            include = val[index] + self.func(W-wt[index], val, wt, index+1, n, dp) 
        
        dp[index][W] = max(include, exclude)
        return dp[index][W]




class Solution:
    def knapsack(self, W, val, wt):
        n = len(wt)
        dp = [[0] * (W+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for cap in range(W+1):
                exclude = dp[i+1][cap]
                include = 0
                if wt[i] <= cap:
                    include = val[i] + dp[i+1][cap-wt[i]]
                dp[i][cap] = max(include, exclude)
        
        return dp[0][W]
    
   
