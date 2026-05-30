class Solution:
    def findSubarray(self, arr):
        n = len(arr)
        count = 0
        hashmap = {}
        hashmap[0] = 1
        s = 0
        for i in range(n):
            s += arr[i]
            if s in hashmap:
                count += hashmap[s]
            hashmap[s] = hashmap.get(s, 0) + 1
        return count
