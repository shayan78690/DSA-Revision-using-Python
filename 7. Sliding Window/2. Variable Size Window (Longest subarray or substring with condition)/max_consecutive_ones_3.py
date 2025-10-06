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
        max_len = 0
        zeroes = 0
        while right < n:
            if nums[right] == 0:
                zeroes += 1
            
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            
            if zeroes <= k:
                max_len = max(max_len, right-left+1)
            right += 1
        return max_len