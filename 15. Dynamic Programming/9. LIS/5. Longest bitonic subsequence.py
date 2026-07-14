class Solution:
    def longestBitonicSequence(self, n, nums):

        dp1 = [1] * n

        for index in range(n):
            for prevIndex in range(index):
                if nums[index] > nums[prevIndex]:
                    dp1[index] = max(dp1[index], dp1[prevIndex] + 1)

        dp2 = [1] * n

        for index in range(n - 1, -1, -1):
            for nextIndex in range(n - 1, index, -1):
                if nums[index] > nums[nextIndex]:
                    dp2[index] = max(dp2[index], dp2[nextIndex] + 1)

        ans = 0

        for i in range(n):
            if dp1[i] > 1 and dp2[i] > 1:
                ans = max(ans, dp1[i] + dp2[i] - 1)

        return ans
