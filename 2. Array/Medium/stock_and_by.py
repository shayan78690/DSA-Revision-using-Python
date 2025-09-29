class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            profit = prices[i] - buy
            max_profit = max(max_profit, profit)
            buy = min(buy, prices[i])
        return max_profit


        