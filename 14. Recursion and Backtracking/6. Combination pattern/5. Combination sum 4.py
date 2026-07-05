class Solution(object):
    def combinationSum4(self, nums, target):
        return self.func(nums, target)
    
    def func(self, nums, target):
        if target == 0:
            return 1
        if target < 0:
            return 0
        count = 0
        for num in nums:
            count += self.func(nums, target-num)
        return count
        
        
        
