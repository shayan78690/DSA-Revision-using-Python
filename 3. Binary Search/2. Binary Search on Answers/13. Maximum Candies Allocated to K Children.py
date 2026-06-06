class Solution(object):

    def isPossible(self, candies, k, pile):
        total = 0
        for candy in candies:
            total += (candy//pile)
        return total >= k

    def maximumCandies(self, candies, k):
        n = len(candies)
        low = 1
        high = max(candies)
        result = 0
        while low <= high:
            mid = (low+high)//2
            if self.isPossible(candies, k, mid):
                result = mid
                low = mid+1
            else:
                high = mid-1
        return result
