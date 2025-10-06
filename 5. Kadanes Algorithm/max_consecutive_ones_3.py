class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = 0
        maxLen = 0
        zeroes = 0

        while right < n:
            if nums[right] == 0:
                zeroes += 1

            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1

            if zeroes <= k:
                maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen