class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        prefix = [0] * n  

        for booking in bookings:
            first = booking[0] - 1 
            last = booking[1] - 1
            val = booking[2]
            prefix[first] += val
            if last + 1 < n:
                prefix[last + 1] -= val

        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        return prefix