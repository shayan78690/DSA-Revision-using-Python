class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        m = {}
        s = 0
        m[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            rem = s-goal
            if rem in m:
                count += m[rem]
            m[s] = m.get(s, 0) + 1
        return count