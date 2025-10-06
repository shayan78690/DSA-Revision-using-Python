class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = 0
        s = 0
        m = {}
        m[0] = -1
        for i in range(n):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1
            
            if s in m:
                length = i - m[s]
                maxi = max(maxi, length)
            else:
                m[s] = i
        return maxi