class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        odd = 0
        even = 1
        prefixSum = 0
        count = 0
        mod = 1000000007
        
        for i in range(n):
            prefixSum += arr[i]
            if prefixSum % 2 == 0:
                count = (count + odd) % mod
                even += 1
            else:
                count = (count + even) % mod
                odd += 1
        
        return count
        