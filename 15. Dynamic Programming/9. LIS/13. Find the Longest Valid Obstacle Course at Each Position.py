class Solution(object):
    def longestObstacleCourseAtEachPosition(self, arr):
        n = len(arr)
        dp = [1] * n
        for index in range(n):
            for prev in range(index):
                if arr[index] >= arr[prev]:
                    dp[index] = max(dp[index], dp[prev]+1)
        return dp



