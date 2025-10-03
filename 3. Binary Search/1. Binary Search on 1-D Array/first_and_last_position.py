class Solution:
    def func1(self, nums, target):
        ans = -1
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return ans

    def func2(self, nums, target):
        ans = -1
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                ans = mid
                low = mid+1
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return ans

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        starting = self.func1(nums, target)
        ending = self.func2(nums, target)
        if starting == -1 or ending == -1:
            return [-1, -1]
        return [starting, ending]
        