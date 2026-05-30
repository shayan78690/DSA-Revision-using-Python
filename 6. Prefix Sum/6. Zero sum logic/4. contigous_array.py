class Solution(object):
    def findMaxLength(self, nums):
        n = len(nums)
        s = 0
        hashmap = {}
        hashmap[0] = -1
        maxi = 0
        for i in range(n):
            if nums[i] == 1:
                s += 1
            else:
                s -= 1
            if s in hashmap:
                length = i - hashmap[s]
                maxi = max(maxi, length)
            else:
                hashmap[s] = i
        return maxi
        
