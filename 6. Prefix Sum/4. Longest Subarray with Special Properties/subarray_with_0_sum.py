class Solution:
    def maxLength(self, arr):
        # code here
        m = {}
        maxi = 0
        s = 0
        n = len(arr)
        for i in range(n):
            s += arr[i]
            if s == 0:
                maxi = i+1
            else:
                if s in m:
                    maxi = max(maxi, i - m[s])
                else:
                    m[s] = i
        return maxi