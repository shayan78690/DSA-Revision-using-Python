class Solution:
    def longestSubarrayDivK(self, arr, k):
        n = len(arr)
        m = {}
        maxi = 0
        s = 0
        m[0] = -1

        for i in range(n):
            s += arr[i]
            rem = s % k

            if rem in m:
                length = i - m[rem]
                maxi = max(maxi, length)
            else:
                m[rem] = i  

        return maxi
