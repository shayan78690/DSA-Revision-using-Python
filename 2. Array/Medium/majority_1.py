class Sol(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        turn = n // 2
        for i in range(n):
            count = 0
            for j in range(0, n):
                if nums[i] == nums[j]:
                    count += 1
            if count > turn:
                return nums[i]
        return -1

        
        
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        turn = n // 2
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for key in freq:
            if freq[key] > turn:
                return freq
            
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0
        element = 0
        for i in nums:
            if count == 0:
                count = 1
                element = i
            elif element == i:
                count += 1
            else:
                count -= 1
        
        count1 = 0
        for i in nums:
            if i == element:
                count1 += 1
        return element if count1 > n // 2 else -1
        