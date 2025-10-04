import math
class Solution(object):
    def func(self, arr, threshold, divisor):
        s = 0
        for i in range(len(arr)):
            s += math.ceil(float(arr[i])/divisor)
        return s
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        low = 1
        high = max(nums)
        ans = high
        while low <= high:
            mid = (low+high)//2
            result = self.func(nums, threshold, mid)
            if result <= threshold:
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans
        