class Solution(object):
    
    def func(self, nums, k):
        n = len(nums)
        count = 0
        left = 0
        right = 0
        map = {}
        
        while right < n:
            map[nums[right]] = map.get(nums[right], 0) + 1
            
            while len(map) > k:
                map[nums[left]] = map[nums[left]] - 1
                if map[nums[left]] == 0:
                    del map[nums[left]]
                left += 1
            
            count += (right - left + 1)
            right += 1
        
        return count

    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.func(nums, k) - self.func(nums, k-1)