class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        ans = float('-inf')
        left = 0
        right = 0
        total = 0.0

        while right < n:
            total += nums[right]

            while right - left + 1 > k:
                total -= nums[left]
                left += 1

            if right - left + 1 == k:
                avg = total / k
                ans = max(ans, avg)

            right += 1

        return ans

        