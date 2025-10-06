class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = nums[0]
        prod1 = nums[0]
        prod2 = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] < 0:
                prod1, prod2 = prod2, prod1
            prod1 = max(prod1*nums[i], nums[i])
            prod2 = min(prod2*nums[i], nums[i])

            maxi = max(maxi, prod1)
        return maxi
        