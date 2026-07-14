class Solution(object):
    def findNumberOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        for index in range(n):
            for prevIndex in range(index):
                if nums[index] > nums[prevIndex]:
                    if dp[prevIndex]+1 > dp[index]:
                        dp[index] = dp[prevIndex]+1
                        count[index] = count[prevIndex]
                    elif dp[prevIndex]+1 == dp[index]:
                        count[index] += count[prevIndex]
        maxLen = max(dp)
        ans = 0
        for i in range(n):
            if dp[i] == maxLen:
                ans += count[i]
        
        return ans
        
