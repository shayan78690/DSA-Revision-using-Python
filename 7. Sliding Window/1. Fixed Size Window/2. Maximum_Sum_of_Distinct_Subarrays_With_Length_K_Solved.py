class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        hashmap = {}
        maxi = 0
        s = 0
        left = 0
        right = 0
        while right < n:
            s += nums[right]
            hashmap[nums[right]] = hashmap.get(nums[right], 0) + 1
            while hashmap[nums[right]] > 1 or right-left+1 > k:
                s -= nums[left]
                hashmap[nums[left]] -= 1
                if hashmap[nums[left]] == 0:
                    del hashmap[nums[left]]
                left += 1
            if len(hashmap) == k and right-left+1 == k:
                maxi = max(maxi, s)
            right += 1
        return maxi
        
