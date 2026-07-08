class Solution:  
    def findMaxSum(self, arr):
        n = len(arr)
        dp = [-1] * n
        return self.func(arr, n, 0, dp)
    
    def func(self, arr, n, index, dp):
        if index >= n:
            return 0
        if dp[index] != -1:
            return dp[index]
        take = arr[index] + self.func(arr, n, index+2, dp)
        skip = self.func(arr, n, index+1, dp)
        dp[index] = max(take, skip)
        return dp[index]


class Solution:  
    def findMaxSum(self, arr):
        n = len(arr)
        dp = [0] * (n+2)
        for i in range(n-1, -1, -1):
            take = arr[i] + dp[i+2]
            skip = dp[i+1]
            dp[i] = max(take, skip)
        return dp[0]
 
