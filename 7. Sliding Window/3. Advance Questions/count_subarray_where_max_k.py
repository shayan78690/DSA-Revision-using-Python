class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        max_val = max(nums)

        res = 0
        left = 0
        count = 0

        for right in range(n):
            if nums[right] == max_val:
                count += 1

            while count >= k:
                res += n - right
                if nums[left] == max_val:
                    count -= 1
                left += 1

        return res