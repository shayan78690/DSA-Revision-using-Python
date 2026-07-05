class Solution(object):
    def combinationSum2(self, candidates, target):
        n = len(candidates)
        result = []
        candidates.sort()
        self.func(candidates, n, result, target, [], 0)
        return result
    
    def func(self, nums, n, result, target, current, idx):
        if target == 0:
            result.append(current[:])
            return
        for i in range(idx, n):
            if i > idx and nums[i] == nums[i-1]:
                continue
            if nums[i] > target:
                break
            current.append(nums[i])
            self.func(nums, n, result, target-nums[i], current, i+1)
            current.pop()
        
