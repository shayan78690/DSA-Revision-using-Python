class Solution:
    def minMaxCandy(self, prices, k):
        prices.sort()
        n = len(prices)
        i = 0
        j = n-1
        mini = 0
        while i <= j:
            mini += prices[i]
            i += 1
            j -= k
        
        i = 0
        j = n-1
        maxi = 0
        while i <= j:
            maxi += prices[j]
            j -= 1
            i += k
        
        return [mini, maxi]
        
        
