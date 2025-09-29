class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        freq = [0] * (n+1)
        for i in range(0, n):
            freq[nums[i]] += 1
        
        for i in range(0, n+1):
            if freq[i] == 0:
                return i



class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum_of_n = (n*(n+1))//2
        sum_of_elements = sum(nums)
        return sum_of_n - sum_of_elements
        