class Solution:
    def check(self, nums):
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                count += 1
        
        if nums[n-1] > nums[0]:
            count += 1

        return count <= 1