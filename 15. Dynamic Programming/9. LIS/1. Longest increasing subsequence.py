class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        return self.func(nums, n, 0, -1)
    
    def func(self, nums, n, index, prev):
        if index == n:
            return 0

        skip = self.func(nums, n, index+1, prev)

        take = 0
        if prev == -1 or nums[index] > nums[prev]:
            take = 1 + self.func(nums, n, index+1, index)
        
        return max(take, skip)


class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[-1] * (n+1) for _ in range(n)]
        return self.func(nums, n, 0, -1, dp)
    
    def func(self, nums, n, index, prev, dp):
        if index == n:
            return 0
        
        if dp[index][prev+1] != -1:
            return dp[index][prev+1]

        skip = self.func(nums, n, index+1, prev, dp)

        take = 0
        if prev == -1 or nums[index] > nums[prev]:
            take = 1 + self.func(nums, n, index+1, index, dp)
        
        dp[index][prev+1] = max(take, skip)
        return dp[index][prev+1]



class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):

            for prevIndex in range(index - 1, -2, -1):

                skip = dp[index + 1][prevIndex + 1]

                take = 0
                if prevIndex == -1 or nums[index] > nums[prevIndex]:
                    take = 1 + dp[index + 1][index + 1]

                dp[index][prevIndex + 1] = max(skip, take)

        return dp[0][0]
