class Solution(object):
    
    def func(self, arr, c, k):
        total = 0

        for candy in arr:
            total += candy // c

        return total >= k

    def maximumCandies(self, candies, k):
        ans = 0
        maxi = max(candies)

        low = 1
        high = maxi

        while low <= high:
            mid = (low + high) // 2

            if self.func(candies, mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
