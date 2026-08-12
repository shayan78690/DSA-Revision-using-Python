class Solution(object):
    def longestSubsequence(self, arr, difference):
        n = len(arr)
        
        dp = [1] * n
        for index in range(n):
            for prev in range(index):
                if arr[index]-arr[prev] == difference:
                    dp[index] = max(dp[index], dp[prev]+1)
        return max(dp)

  class Solution(object):
    def longestSubsequence(self, arr, difference):
        n = len(arr)
        dp = {}
        ans = 0
        for x in arr:
            dp[x] = dp.get(x-difference, 0) + 1
            ans = max(ans, dp[x])
        return ans
        
