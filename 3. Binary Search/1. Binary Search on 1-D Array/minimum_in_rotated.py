class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = float('inf')
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                mini = min(nums[low], mini)
                break
            if nums[low] <= nums[mid]:
                mini = min(nums[low], mini)
                low = mid + 1
            else:
                mini = min(mini, nums[mid])
                high = mid - 1
        return mini