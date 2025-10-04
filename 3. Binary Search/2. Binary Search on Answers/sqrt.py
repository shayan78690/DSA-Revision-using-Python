class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x
        while low <= high:
            mid = (low + high) // 2
            val = mid*mid
            if val <= x:
                low = mid+1
            else:
                high = mid-1
        return high