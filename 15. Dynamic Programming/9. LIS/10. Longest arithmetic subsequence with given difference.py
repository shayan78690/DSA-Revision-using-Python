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
        # current-prev = diff
        # prev = current-diff
        dp = {}
        n = len(arr)
        maxi = 0
        for current in arr:
            prev = current-difference
            dp[current] = dp.get(prev, 0) + 1
            maxi = max(maxi, dp[current])
        return maxi
        


class Solution(object):
    def longestSubsequence(self, arr, difference):
        # current-prev = diff
        # prev = current-diff
        dp = {}
        n = len(arr)
        maxi = 0
        for current in arr:
            prev = current-difference
            if prev in dp:
                dp[current] = dp[prev] + 1
            else:
                dp[current] = 1
            maxi = max(maxi, dp[current])
        return maxi
        
