class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return self.func(nums, 0, n)
    
    def func(self, nums, idx, n):
        if idx >= n-1:
            return 0
        if nums[idx] == 0:
            return float('inf')
        
        minSteps = float('inf')
        for i in range(1, nums[idx] + 1):
            minSteps = min(minSteps, 1 + self.func(nums, idx + i, n))
        return minSteps


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n
        return self.func(nums, 0, n, dp)
    
    def func(self, nums, idx, n, dp):
        if idx >= n-1:
            return 0
        if nums[idx] == 0:
            return float('inf')

        if dp[idx] != -1:
            return dp[idx]
        
        minSteps = float('inf')
        for i in range(1, nums[idx] + 1):
            minSteps = min(minSteps, 1 + self.func(nums, idx + i, n, dp))
        dp[idx] = minSteps
        return dp[idx]
        
