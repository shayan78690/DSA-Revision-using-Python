class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        for j in range(1, n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1
