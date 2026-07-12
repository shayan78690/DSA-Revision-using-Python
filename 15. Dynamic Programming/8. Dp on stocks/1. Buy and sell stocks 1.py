class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        buy_price = prices[0]
        maxi = 0
        for i in range(1, n):
            profit = prices[i] - buy_price
            maxi = max(maxi, profit)
            buy_price = min(buy_price, prices[i])
        return maxi
        
