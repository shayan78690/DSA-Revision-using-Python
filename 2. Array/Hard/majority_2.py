class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
            if count > n//3 and nums[i] not in ans:
                ans.append(nums[i])
        return ans
    
    
class Solution1:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        
        ans = []
        for i in freq:
            if freq[i] > len(nums) // 3:
                ans.append(i)
        return ans
    
    
    
    
    
    
    
    
class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        element1 = float('-inf')
        element2 = float('-inf')
        count1 = 0
        count2 = 0
        for num in nums:
            if count1 == 0 and element2 != num:
                count1 = 1
                element1 = num
            elif count2 == 0 and element1 != num:
                count2 = 1
                element2 = num
            elif num == element1:
                count1 += 1
            elif num == element2:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        ans = []
        count1 = 0
        count2 = 0
        for num in nums:
            if num == element1:
                count1 += 1
            if num == element2:
                count2 += 1
        mini = len(nums) // 3
        if count1 > mini:
            ans.append(element1)
        if count2 > mini:
            ans.append(element2)
        return ans
