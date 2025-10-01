class Solution(object):
    def linearSearch(self, nums, x):
        for i in nums:
            if i == x:
                return True
        return False

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 1
        for i in nums:
            x = i
            count = 1
            while self.linearSearch(nums, x+1):
                x += 1
                count += 1
            
            longest = max(longest, count)
        
        return longest
        
class Solution1:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        s = set()
        longest = 1
        for i in range(n):
            s.add(nums[i])
        
        for i in s:
            if i-1 not in s:
                count = 1
                x = i
                while x+1 in s:
                    x += 1
                    count += 1
                longest = max(longest, count)
        return longest
