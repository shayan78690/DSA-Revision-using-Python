class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]
        
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i] * suffix[i + 1]
        
        ans = [0] * n
        ans[0] = suffix[1]
        ans[n - 1] = prefix[n - 2]
        for i in range(1, n - 1):
            ans[i] = prefix[i - 1] * suffix[i + 1]
        
        return ans