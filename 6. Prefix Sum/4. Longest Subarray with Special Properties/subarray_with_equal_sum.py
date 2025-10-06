class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m = {}
        n = len(nums)
        for i in range(0, n-1):
            s = nums[i] + nums[i+1]
            if s in m:
                return True
            else:
                m[s] = m.get(s, 0) + 1
        return False
        