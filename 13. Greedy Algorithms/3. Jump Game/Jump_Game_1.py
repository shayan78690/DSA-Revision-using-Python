class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxIdx = 0
        for i in range(len(nums)):
            if i > maxIdx:
                return False
            maxIdx = max(maxIdx, nums[i] + i)
        return True
        
