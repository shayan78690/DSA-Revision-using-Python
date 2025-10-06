class Solution(object):
    def subarraysDivByK(self, nums, k):
        n = len(nums)
        map = {}
        map[0] = 1
        sum = 0
        count = 0
        for i in nums:
            sum += i
            rem = sum % k
            if rem in map:
                count += map[rem]
            map[rem] = map.get(rem, 0) + 1

        return count
        