class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n

        idx = n - 1
        i = 0
        j = n - 1

        while i <= j:
            leftSq = nums[i] * nums[i]
            rightSq = nums[j] * nums[j]

            if leftSq > rightSq:
                ans[idx] = leftSq
                i += 1
            else:
                ans[idx] = rightSq
                j -= 1
            idx -= 1

        return ans
