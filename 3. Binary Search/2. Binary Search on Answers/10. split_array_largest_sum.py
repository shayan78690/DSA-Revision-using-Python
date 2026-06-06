class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if n < k:
            return -1
        low = max(nums)
        high = sum(nums)
        ans = low
        while low <= high:
            mid = (low + high) // 2
            temp = self.func(nums, mid)
            if temp <= k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
    
    def func(self, nums, val):
        s = 0
        count = 1
        for i in range(len(nums)):
            if nums[i] + s <= val:
                s += nums[i]
            else:
                count += 1
                s = nums[i]
        return count
