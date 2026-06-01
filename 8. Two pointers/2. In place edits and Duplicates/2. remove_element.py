class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
class Solution(object):
    def removeElement(self, nums, val):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != element:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i
        
