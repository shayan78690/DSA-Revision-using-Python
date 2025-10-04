class Solution(object):
    
    def func(self, arr, days, cap):
        n = len(arr)
        load = 0
        d = 1
        for i in range(n):
            if load + arr[i] > cap:
                d += 1
                load = arr[i]
            else:
                load += arr[i]
        return d

    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        low = max(weights)
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            temp = self.func(weights, days, mid)
            if temp <= days:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans