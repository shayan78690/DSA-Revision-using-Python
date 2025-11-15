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
        maxavg = float('-inf')
        s = 0.0
        while right < n:
            s += nums[right]
            if right-left+1 > k :
                s -= nums[left]
                left += 1
            
            if right-left+1 == k:
                avg = s / k
                maxavg = max(maxavg, avg)
            right += 1
        
        return maxavg
