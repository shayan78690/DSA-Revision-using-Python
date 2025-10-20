from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * (n - k + 1)
        idx = 0
        dq = deque()
        for i in range(n):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                res[idx] = nums[dq[0]]
                idx += 1
        return res