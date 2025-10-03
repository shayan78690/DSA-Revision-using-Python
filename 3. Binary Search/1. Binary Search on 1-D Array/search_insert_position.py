class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1
        index = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                index = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return index