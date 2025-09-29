class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

        return ans
        


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        n = len(nums)
        ans = []
        for i in range(n):
            num = nums[i]
            more_needed = target - num
            if more_needed in hashmap:
                ans.append(hashmap[more_needed])
                ans.append(i)
                return ans
            hashmap[num] = i
        return ans
        