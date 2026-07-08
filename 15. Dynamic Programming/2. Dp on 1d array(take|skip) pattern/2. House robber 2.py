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




class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        nums1 = nums[:-1]
        n = len(nums1)
        nums2 = nums[1:]
        m = len(nums2)
        dp1 = [0] * (n+2)
        dp2 = [0] * (m+2)
        for i in range(n-1, -1, -1):
            take = nums1[i] + dp1[i+2]
            skip = dp1[i+1]
            dp1[i] = max(take, skip)

        for i in range(m-1, -1, -1):
            take = nums2[i] + dp2[i+2]
            skip = dp2[i+1]
            dp2[i] = max(take, skip)

        return max(dp1[0], dp2[0])    
   
