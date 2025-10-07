class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mini = float('inf')
        n = len(nums)
        for i in range(n):
            orValue = 0
            for j in range(i, n):
                orValue |= nums[j]
                if orValue >= k:
                    mini = min(mini, j-i+1)
                    break
        return mini if mini != float('inf') else -1 
        