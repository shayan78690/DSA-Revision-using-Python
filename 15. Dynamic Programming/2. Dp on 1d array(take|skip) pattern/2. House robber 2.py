class Solution(object):
    def rob(self, nums):
        return max(self.func(nums[:-1], 0), self.func(nums[1:], 0))
    
    def func(self, nums, index):
        if index >= len(nums):
            return 0
        take = nums[index] + self.func(nums, index+2)
        skip = self.func(nums, index+1)
        return max(take, skip)


class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp1 = [-1] * (len(nums)-1)
        dp2 = [-1] * (len(nums)-1)
        return max(self.func(nums[:-1], 0, dp1), self.func(nums[1:], 0, dp2))
    
    def func(self, nums, index, dp):
        if index >= len(nums):
            return 0
        if dp[index] != -1:
            return dp[index]
        take = nums[index] + self.func(nums, index+2, dp)
        skip = self.func(nums, index+1, dp)
        dp[index] = max(take, skip)
        return dp[index]
        
