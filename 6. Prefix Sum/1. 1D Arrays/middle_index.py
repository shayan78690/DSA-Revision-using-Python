class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = [0] * n
        right = [0] * n

        left[0] = nums[0]
        right[n - 1] = nums[n - 1]

        for i in range(1, n):
            left[i] = nums[i] + left[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = nums[i] + right[i + 1]

        for i in range(n):
            if left[i] == right[i]:
                return i

        return -1
        