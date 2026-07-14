class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = arr[:]

        maxi = max(arr)

        for index in range(n):
            for prevIndex in range(index):
                if arr[index] > arr[prevIndex]:
                    dp[index] = max(dp[index],
                                    dp[prevIndex] + arr[index])

            maxi = max(maxi, dp[index])

        return maxi
