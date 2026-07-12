class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        return self.func(prices, n, 0, 1)
    
    def func(self, prices, n, day, buy):
        if day == n:
            return 0

        if buy:
            buyToday = -prices[day] + self.func(prices, n, day+1, 0)
            skip = self.func(prices, n, day+1, 1)
            return max(buyToday, skip)
        else:
            sellToday = prices[day] + self.func(prices, n, day+1, 1)
            skip = self.func(prices, n, day+1, 0)
            return max(sellToday, skip)



class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return self.func(prices, n, 0, 1, dp)
    
    def func(self, prices, n, day, buy, dp):
        if day == n:
            return 0
        if dp[day][buy] != -1:
            return dp[day][buy]
        if buy:
            buyToday = -prices[day] + self.func(prices, n, day+1, 0, dp)
            skip = self.func(prices, n, day+1, 1, dp)
            dp[day][buy] = max(buyToday, skip)
            return dp[day][buy]
        else:
            sellToday = prices[day] + self.func(prices, n, day+1, 1, dp)
            skip = self.func(prices, n, day+1, 0, dp)
            dp[day][buy] = max(sellToday, skip)
            return dp[day][buy]



class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        for day in range(n-1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    buyToday = -prices[day] + dp[day+1][0]
                    skip = dp[day+1][1]
                    dp[day][buy] = max(buyToday, skip)
                else:
                    sellToday = prices[day] + dp[day+1][1]
                    skip = dp[day+1][0]
                    dp[day][buy] = max(sellToday, skip)
        return dp[0][1] 
    
    
