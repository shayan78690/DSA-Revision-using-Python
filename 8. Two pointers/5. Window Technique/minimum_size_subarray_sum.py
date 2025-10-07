class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = float('inf')
        n = len(nums)
        left = 0
        right = 0
        s = 0
        while right < n:
            s += nums[right]
            while s >= target:
                min_length = min(min_length, right-left+1)
                s -= nums[left]
                left += 1
            right += 1
        return 0 if min_length == float('inf') else min_length
        