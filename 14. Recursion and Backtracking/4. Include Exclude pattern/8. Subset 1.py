class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        result = []
        self.func(nums, n, result, [], 0)
        return result

    def func(self, nums, n, result, current, idx):
        if idx == n:
            result.append(current[:])
            return 
        current.append(nums[idx])
        self.func(nums, n, result, current, idx+1)
        current.pop()
        self.func(nums, n, result, current, idx+1)
