class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
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
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        dp = [[False] * (target+1) for _ in range(n+1)]
        for index in range(n+1):
            dp[index][0] = True
        
        for index in range(n-1, -1, -1):
            for cap in range(1, target+1):
                exclude = dp[index+1][cap]
                include = False
                if nums[index] <= cap:
                    include = dp[index+1][cap-nums[index]]
                dp[index][cap] = include or exclude
        return dp[0][target]

   
