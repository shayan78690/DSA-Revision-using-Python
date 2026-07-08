class Solution:
    def minCost(self, height):
        n = len(height)
        return self.func(height, n, 0)
    
    def func(self, arr, n, index):
        if index == n-1:
            return 0
        
        onestep = self.func(arr, n, index+1) + abs(arr[index]-arr[index+1])
        twostep = float('inf')
        if index+2 < n:
            twostep = self.func(arr, n, index+2) + abs(arr[index]-arr[index+2])
        return min(onestep, twostep)


class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [-1] * n
        return self.func(height, n, 0, dp)
    
    def func(self, arr, n, index, dp):
        if index == n-1:
            return 0
        if dp[index] != -1:
            return dp[index]
        
        onestep = self.func(arr, n, index+1, dp) + abs(arr[index]-arr[index+1])
        twostep = float('inf')
        if index+2 < n:
            twostep = self.func(arr, n, index+2, dp) + abs(arr[index]-arr[index+2])
        dp[index] = min(onestep, twostep)
        return dp[index]


class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [0] * (n+2)
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            onestep = dp[i+1] + abs(height[i]-height[i+1])
            twostep = float('inf')
            if i+2 < n:
                twostep = dp[i+2] + abs(height[i]-height[i+2])
            dp[i] = min(onestep, twostep)
        return dp[0]
    
class Solution:
    def minCost(self, height):
        n = len(height)
        dp = [0] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            onestep = dp[i+1] + abs(height[i]-height[i+1])
            twostep = float('inf')
            if i+2 < n:
                twostep = dp[i+2] + abs(height[i]-height[i+2])
            dp[i] = min(onestep, twostep)
        return dp[0]
    
