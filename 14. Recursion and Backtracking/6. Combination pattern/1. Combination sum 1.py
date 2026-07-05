class Solution(object):
    def combinationSum(self, candidates, target):
        n = len(candidates)
        result = []
        self.func(candidates, n, target, result, [], 0)
        return result
    
    def func(self, nums, n, target, result, current, idx):
        if target == 0:
            result.append(current[:])
            return
        if idx == n or target < 0:
            return
        current.append(nums[idx])
        self.func(nums, n, target-nums[idx], result, current, idx)
        current.pop()
        self.func(nums, n, target, result, current, idx+1)

         
