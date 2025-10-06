class Solution(object):
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        map = {}
        map[0] = -1
        sum = 0
        for i in range(0, n):
            sum += nums[i]
            rem = sum % k
            if rem in map:
                if i - map[rem] > 1:
                    return True
            else:
                map[rem] = i
        return False
        