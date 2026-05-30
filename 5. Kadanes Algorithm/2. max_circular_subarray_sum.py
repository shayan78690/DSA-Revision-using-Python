class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = nums[0]
        sum_1 = nums[0]
        mini = nums[0]
        sum_2 = nums[0]
        total = nums[0]

        for i in range(1, n):
            sum_1 = max(nums[i], sum_1 + nums[i])
            maxi = max(sum_1, maxi)

            sum_2 = min(nums[i], sum_2 + nums[i])
            mini = min(mini, sum_2)

            total += nums[i]

        if maxi < 0:
            return maxi

        return max(maxi, total - mini)
