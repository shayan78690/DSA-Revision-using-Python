import math
class Solution(object):

    def func(self, piles, hour):
        time = 0
        for i in range(len(piles)):
            time += math.ceil(float(piles[i])/hour)
        return time

    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = len(piles)
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low+high)//2
            reqTime = self.func(piles, mid)
            if reqTime <= h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
