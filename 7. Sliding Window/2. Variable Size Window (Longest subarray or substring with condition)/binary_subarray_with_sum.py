class Solution(object):
    
    def func(self, nums, k):
        if k < 0:
            return 0
        s = 0
        count = 0
        left = 0
        right = 0
        n = len(nums)
        while right < n:
            s += nums[right]
            while s > k:
                s -= nums[left]
                left += 1
            count += (right-left+1)
            right += 1
        return count


    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        return self.func(nums, goal) - self.func(nums, goal-1)