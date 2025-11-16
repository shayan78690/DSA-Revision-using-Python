class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.func(nums, k) - self.func(nums, k-1)
    
    def func(self, nums, k):
        n = len(nums)
        left = 0
        right = 0
        count = 0
        odd = 0
        while right < n:
            if nums[right] % 2 != 0:
                odd += 1
            while odd > k:
                if nums[left] % 2 != 0:
                    odd -= 1
                left += 1
            count += (right-left+1)
            right += 1
        return count
