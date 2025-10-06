class Solution(object):
    
    def func(self, nums, k):
        count = 0
        left = 0
        right = 0
        n = len(nums)
        sum = 0
        
        while right < n:
            sum += nums[right] % 2
            
            while sum > k:
                sum -= nums[left] % 2
                left += 1
            
            count += (right - left + 1)
            right += 1
        
        return count

    def numberOfSubarrays(self, nums, k):
        return self.func(nums, k) - self.func(nums, k - 1)
        