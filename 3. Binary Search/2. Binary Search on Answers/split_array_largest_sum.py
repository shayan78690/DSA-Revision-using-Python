class Solution(object):
    
    def func(self, nums, k, mid):
        count = 1
        s = 0
        for i in range(len(nums)):
            if s + nums[i] <= mid:
                s += nums[i]
            else:
                count += 1
                s = nums[i]
        return count

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
            temp = self.func(nums, k, mid)
            if temp <= k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans        