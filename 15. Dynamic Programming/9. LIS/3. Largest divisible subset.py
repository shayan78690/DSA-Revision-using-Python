class Solution(object):
    def largestDivisibleSubset(self, nums):
        n = len(nums)
        nums.sort()
        dp = [1] * n
        parent = [i for i in range(n)]
        maxLen = 1
        lastIndex = 0
        for index in range(n):
            for prevIndex in range(index):
                if nums[index] % nums[prevIndex] == 0:
                    if dp[prevIndex] + 1 > dp[index]:
                        dp[index] = dp[prevIndex] + 1
                        parent[index] = prevIndex
            if dp[index] > maxLen:
                maxLen = dp[index]
                lastIndex = index
        
        result = []
        while parent[lastIndex] != lastIndex:
            result.append(nums[lastIndex])
            lastIndex = parent[lastIndex]
        result.append(nums[lastIndex])
        result.reverse()
        return result
        
