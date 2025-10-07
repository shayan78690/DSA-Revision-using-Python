class Solution:
    def numSubarrayBoundedMax(self, nums, left, right):
        return self.count(nums, right) - self.count(nums, left - 1)

    def count(self, nums, bound):
        res = 0
        curr = 0

        for num in nums:
            if num <= bound:
                curr += 1
            else:
                curr = 0
            res += curr

        return res
