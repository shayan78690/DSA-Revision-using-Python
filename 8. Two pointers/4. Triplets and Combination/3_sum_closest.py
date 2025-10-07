class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s-target) < abs(closest-target):
                    closest = s
                elif s > target:
                    k -= 1
                else:
                    j += 1
        return closest