class Solution(object):
    def moveZeroes(self, nums):
        j = -1
        n = len(nums)
        for i in range(0, n):
            if nums[i] == 0:
                j = i
                break

        if j == -1:
            return nums
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        