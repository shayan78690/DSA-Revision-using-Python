class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        j = -1
        for i in range(n):
            if nums[i] % 2 != 0:
                j = i
                break
        if j == -1:
            return nums
        for i in range(j+1, n):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
        

class Solution(object):
    def sortArrayByParity(self, nums):
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
        
