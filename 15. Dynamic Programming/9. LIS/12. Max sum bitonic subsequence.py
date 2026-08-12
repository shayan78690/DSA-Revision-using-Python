class Solution:
    def maxSumBS(self, arr):
        n = len(arr)
        dp1 = arr[:]
        for i in range(n):
            for j in range(i):
                if arr[i] > arr[j]:
                    dp1[i] = max(dp1[i], dp1[j] + arr[i])
        
        dp2 = arr[:]
        for i in range(n-1, -1, -1):
            for j in range(n-1, i, -1):
                if arr[i] > arr[j]:
                    dp2[i] = max(dp2[i], dp2[j] + arr[i])
        
        ans = 0
        for i in range(n):
            ans = max(ans, dp1[i]+dp2[i]-arr[i])
        return ans
        
