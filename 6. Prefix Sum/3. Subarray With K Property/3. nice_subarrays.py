class Solution(object):
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        count = 0
        odd_count = 0
        map = {}
        map[0] = 1
        for num in nums:
            if num % 2 != 0:
                odd_count += 1
            if odd_count-k in map:
                count += map[odd_count-k]
            map[odd_count] = map.get(odd_count, 0) + 1
        
        return count
        
