class Solution(object):

    def isPossible(self, nums, maxOperations, divisor):
        total = 0
        for num in nums:
            total += ((num-1)//divisor)
        return total <= maxOperations

    def minimumSize(self, nums, maxOperations):
        n = len(nums)
        low = 1
        high = max(nums)
        result = high
        while low <= high:
            mid = (low+high) // 2
            if self.isPossible(nums, maxOperations, mid):
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
        
