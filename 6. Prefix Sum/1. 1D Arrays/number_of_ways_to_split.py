class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum = 0
        count = 0

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum

            if left_sum >= right_sum:
                count += 1

        return count