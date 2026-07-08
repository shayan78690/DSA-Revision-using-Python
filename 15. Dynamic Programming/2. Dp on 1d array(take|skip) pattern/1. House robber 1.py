class Solution(object):
    def rob(self, nums):
        n = len(nums)
        return self.func(nums, n, 0)
    
    def func(self, nums, n, index):
        if index >= n:
            return 0
        take = nums[index] + self.func(nums, n, index+2)
        skip = self.func(nums, n, index+1)
        return max(take, skip)        

class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [-1] * n
        return self.func(nums, n, 0, dp)
    
    def func(self, nums, n, index, dp):
        if index >= n:
            return 0
        if dp[index] != -1:
            return dp[index]
        take = nums[index] + self.func(nums, n, index+2, dp)
        skip = self.func(nums, n, index+1, dp)
        dp[index] = max(take, skip)
        return dp[index]        
