class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        return self.func(nums, n, 0, target)
    
    def func(self, nums, n, index, target):
        if target == 0:
            return True
        if index == n:
            return False
        
        exclude = self.func(nums, n, index+1, target)
        include = False
        if nums[index] <= target:
            include = self.func(nums, n, index+1, target-nums[index])
        return include or exclude


class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[None] * (target+1) for _ in range(n)]
        return self.func(nums, n, 0, target, dp)
    
    def func(self, nums, n, index, target, dp):
        if target == 0:
            return True
        if index == n:
            return False
        if dp[index][target] is not None:
            return dp[index][target]
        
        exclude = self.func(nums, n, index+1, target, dp)
        include = False
        if nums[index] <= target:
            include = self.func(nums, n, index+1, target-nums[index], dp)
        dp[index][target] = include or exclude
        return dp[index][target]


class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target+1) for _ in range(n+1)]
        for index in range(n+1):
            dp[index][0] = True
        
        for index in range(n-1, -1, -1):
            for tar in range(target+1):
                exclude = dp[index+1][tar]
                include = False
                if nums[index] <= tar:
                    include = dp[index+1][tar-nums[index]]
                dp[index][tar] = include or exclude
        return dp[0][target]
    
 
