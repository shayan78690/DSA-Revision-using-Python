class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        return self.func(arr, n, 0, sum)
    
    def func(self, arr, n, index, sum):
        if sum == 0:
            return True
        if index == n:
            return False
        
        exclude = self.func(arr, n, index+1, sum)
        include = False
        if arr[index] <= sum:
            include = self.func(arr, n, index+1, sum-arr[index])
        
        return include or exclude



class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[None] * (sum+1) for _ in range(n)]
        return self.func(arr, n, 0, sum, dp)
    
    def func(self, arr, n, index, sum, dp):
        if sum == 0:
            return True
        if index == n:
            return False
        
        if dp[index][sum] is not None:
            return dp[index][sum]
        
        exclude = self.func(arr, n, index+1, sum, dp)
        include = False
        if arr[index] <= sum:
            include = self.func(arr, n, index+1, sum-arr[index], dp)
        
        dp[index][sum] = include or exclude
        return dp[index][sum]


class Solution:
    def isSubsetSum (self, arr, sum):
        n = len(arr)
        dp = [[False] * (sum+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        
        for index in range(n-1, -1, -1):
            for target in range(1, sum+1):
                exclude = dp[index+1][target]
                include = False
                if arr[index] <= target:
                    include = dp[index+1][target-arr[index]]
                dp[index][target] = include or exclude
                
        return dp[0][sum]


