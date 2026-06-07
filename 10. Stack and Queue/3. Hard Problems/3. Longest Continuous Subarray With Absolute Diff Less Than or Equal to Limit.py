from collections import deque

class Solution(object):
    def longestSubarray(self, nums, limit):
        n = len(nums)

        mindq = deque()
        maxdq = deque()

        left = 0
        maxlen = 0

        for right in range(n):

            while maxdq and maxdq[-1] < nums[right]:
                maxdq.pop()
            maxdq.append(nums[right])

            while mindq and mindq[-1] > nums[right]:
                mindq.pop()
            mindq.append(nums[right])

            while maxdq[0] - mindq[0] > limit:

                if nums[left] == maxdq[0]:
                    maxdq.popleft()

                if nums[left] == mindq[0]:
                    mindq.popleft()

                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen
