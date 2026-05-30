class Solution:
    def maxLength(self, arr):
        n = len(arr)
        maxi = 0
        hashmap = {}
        hashmap[0] = -1
        s = 0
        for i in range(n):
            s += arr[i]
            if s in hashmap:
                length = i - hashmap[s]
                maxi = max(maxi, length)
            else:
                hashmap[s] = i
        return maxi
        
