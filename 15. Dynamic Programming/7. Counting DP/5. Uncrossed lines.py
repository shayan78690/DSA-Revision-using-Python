class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[-1] * m for _ in range(n)]
        return self.func(nums1, nums2, 0, 0, dp)
    
    def func(self, nums1, nums2, i, j, dp):
        if i == len(nums1) or j == len(nums2):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if nums1[i] == nums2[j]:
            dp[i][j] = 1 + self.func(nums1, nums2, i+1, j+1, dp)
        else:
            skip1 = self.func(nums1, nums2, i+1, j, dp)
            skip2 = self.func(nums1, nums2, i, j+1, dp)
            dp[i][j] = max(skip1, skip2)       
        return dp[i][j]

        
