class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k <= 1:
            return 0
        prod = 1
        result = 0
        left = 0
        right = 0
        while right < n:
            prod *= nums[right]
            while prod >= k:
                prod //= nums[left]
                left += 1
            if prod < k:
                result += (right-left+1)
            right += 1
        return result