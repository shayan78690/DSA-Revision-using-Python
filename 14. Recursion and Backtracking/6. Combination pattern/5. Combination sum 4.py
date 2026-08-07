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
        
        
        


class Solution(object):
    def combinationSum4(self, nums, target):
        dp = [-1] * (target + 1)
        return self.func(nums, target, dp)

    def func(self, nums, target, dp):
        if target == 0:
            return 1

        if target < 0:
            return 0

        if dp[target] != -1:
            return dp[target]

        ans = 0

        for num in nums:
            ans += self.func(nums, target - num, dp)

        dp[target] = ans
        return ans
