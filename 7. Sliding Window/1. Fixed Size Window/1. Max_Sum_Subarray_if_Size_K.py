class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        left = 0
        right = 0
        maxi = 0
        s = 0
        while right < n:
            s += arr[right]
            if right-left+1> k:
                s -= arr[left]
                left += 1
            if right-left+1 == k:
                maxi = max(maxi, s)
            right += 1
        return maxi
