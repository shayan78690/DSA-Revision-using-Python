from math import ceil

class Solution(object):

    def isPossible(self, n, quantities, limit):
        ways = 0
        for quantity in quantities:
            ways += ceil(quantity/float(limit))
        return ways <= n

    def minimizedMaximum(self, n, quantities):
        low = 1
        high = max(quantities)
        result = high
        while low <= high:
            mid = (low+high)//2
            if self.isPossible(n, quantities, mid):
                result = mid
                high = mid-1
            else:
                low = mid+1
        return result
        
