class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        left = 0
        right = 0
        maxi = float('-inf')
        total = 0.0
        while right < n:
            total += nums[right]

            while right-left+1 > k:
                total -= nums[left]
                left += 1
            
            if right-left+1 == k:
                avg = total / k
                maxi = max(maxi, avg)
            
            right += 1
        return maxi