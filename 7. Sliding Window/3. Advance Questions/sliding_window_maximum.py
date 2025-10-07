from sortedcontainers import SortedDict

class Solution1:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        map_ = SortedDict()
        left = 0 
        right = 0
        res = [0] * (n-k+1)
        idx = 0
        while right < n:
            map_[nums[right]] = map_.get(nums[right], 0) + 1

            if right-left+1 > k:
                map_[nums[left]] -= 1
                if map_[nums[left]] == 0:
                    del map_[nums[left]]
                left += 1
            if right-left+1 == k:
                res[idx] = map_.peekitem(-1)[0] # larget key
                idx += 1
            right += 1
        return res
            
        


from collections import deque

class Solution2:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        res = [0] * (n - k + 1)
        idx = 0
        dq = deque()

        for i in range(n):
            if dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res[idx] = nums[dq[0]]
                idx += 1

        return res
