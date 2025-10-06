class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        freq = {}
        freq[0] = 1
        prefixSum = 0
        count = 0
        for i in nums:
            prefixSum += i
            rem = prefixSum - k
            if rem in freq:
                count += freq[rem]
            
            freq[prefixSum] = freq.get(prefixSum, 0) + 1
        
        return count


