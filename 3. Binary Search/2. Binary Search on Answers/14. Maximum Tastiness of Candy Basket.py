class Solution(object):

    def possible(self, price, k, minDist):
        candy = 1
        last = price[0]
        for i in range(1, len(price)):
            if price[i]-last >= minDist:
                candy += 1
                last = price[i]
        return candy >= k

    def maximumTastiness(self, price, k):
        price.sort()
        low = 1
        high = price[-1]-price[0]
        result = 0
        while low <= high:
            mid = (low+high)//2
            if self.possible(price, k, mid):
                result = mid
                low = mid+1
            else:
                high = mid-1
        return result
        
