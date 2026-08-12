class Solution(object):
    def longestArithSeqLength(self, nums):
        n = len(nums)
        dp = [{} for _ in range(n)]
        ans = 2
        for index in range(n):
            for prev in range(index):
                diff = nums[index]-nums[prev]
                if diff in dp[prev]:
                    dp[index][diff] = dp[prev][diff] + 1
                else:
                    dp[index][diff] = 2
                ans = max(ans, dp[index][diff])
        return ans
        
