class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        return self.solve(nums, n, target, 0, 0)
    
    def solve(self, nums, n, target, index, current_sum):
        if index == n:
            if current_sum == target:
                return 1
            return 0
        positive = self.solve(nums, n, target, index+1, current_sum+nums[index])
        negative = self.solve(nums, n, target, index+1, current_sum-nums[index])
        return positive + negative

class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        total = sum(nums)
        if abs(target) > total:
            return 0
        offset = total
        dp = [[-1] * (2*total+1) for _ in range(n+1)]
        return self.solve(nums, n, target, 0, 0, offset, dp)
    
    def solve(self, nums, n, target, index, current_sum, offset, dp):
        if index == n:
            if current_sum == target:
                return 1
            return 0
        if dp[index][current_sum+offset] != -1:
            return dp[index][current_sum+offset]
        positive = self.solve(nums, n, target, index+1, current_sum+nums[index], offset, dp)
        negative = self.solve(nums, n, target, index+1, current_sum-nums[index], offset, dp)
        dp[index][current_sum+offset] = positive  + negative
        return dp[index][current_sum+offset]
        
        

class Solution:

    def findTargetSumWays(self, nums, target):

        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total - target) % 2 != 0:
            return 0

        targetSum = (total - target) // 2

        return self.func(nums, 0, targetSum)

    def func(self, nums, index, target):

        if index == len(nums):
            if target == 0:
                return 1
            return 0

        notTake = self.func(nums, index + 1, target)

        take = 0

        if nums[index] <= target:
            take = self.func(
                nums,
                index + 1,
                target - nums[index]
            )

        return take + notTake




class Solution:

    def findTargetSumWays(self, nums, target):

        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total - target) % 2 != 0:
            return 0

        targetSum = (total - target) // 2
        n = len(nums)

        dp = [[-1] * (targetSum + 1) for _ in range(n)]

        return self.func(nums, 0, targetSum, dp)

    def func(self, nums, index, target, dp):

        if index == len(nums):
            return 1 if target == 0 else 0

        if dp[index][target] != -1:
            return dp[index][target]

        notTake = self.func(nums, index + 1, target, dp)

        take = 0
        if nums[index] <= target:
            take = self.func(nums, index + 1, target - nums[index], dp)

        dp[index][target] = take + notTake
        return dp[index][target]



class Solution:

    def findTargetSumWays(self, nums, target):

        total = sum(nums)

        if abs(target) > total:
            return 0

        if (total - target) % 2 != 0:
            return 0

        targetSum = (total - target) // 2
        n = len(nums)

        dp = [[0] * (targetSum + 1) for _ in range(n + 1)]

        dp[n][0] = 1

        for index in range(n - 1, -1, -1):
            for t in range(targetSum + 1):

                notTake = dp[index + 1][t]

                take = 0
                if nums[index] <= t:
                    take = dp[index + 1][t - nums[index]]

                dp[index][t] = take + notTake

        return dp[0][targetSum]
