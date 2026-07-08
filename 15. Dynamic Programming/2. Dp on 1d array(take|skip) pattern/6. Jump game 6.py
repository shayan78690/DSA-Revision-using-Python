class Solution(object):
    def maxResult(self, nums, k):
        n = len(nums)
        return self.func(nums, n, k, 0)
    
    def func(self, nums, n, k, index):
        if index == n-1:
            return nums[index]
        maxi = float('-inf')
        for jump in range(1, k+1):
            if jump+index < n:
                maxi = max(maxi, nums[index] + self.func(nums, n, k, index+jump))
        return maxi


class Solution(object):
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [-1] * n
        return self.func(nums, n, k, 0, dp)
    
    def func(self, nums, n, k, index, dp):
        if index == n-1:
            return nums[index]
        if dp[index] != -1:
            return dp[index]
        maxi = float('-inf')
        for jump in range(1, k+1):
            if jump+index < n:
                maxi = max(maxi, nums[index] + self.func(nums, n, k, index+jump, dp))
        dp[index] = maxi
        return dp[index]


class Solution(object):
    def maxResult(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            maxi = float('-inf')
            for jump in range(1, k+1):
                if jump+i < n:
                    maxi = max(maxi, nums[i]+dp[i+jump])
            dp[i] = maxi
        return dp[0]    
  
