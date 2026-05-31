class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        mini = float('inf')
        s = 0
        while right < n:
            s += nums[right]
            while s >= target:
                mini = min(mini, right-left+1)
                s -= nums[left]
                left += 1
            right += 1
        return 0 if mini == float('inf') else mini
