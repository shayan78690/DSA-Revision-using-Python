class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        return self.func(prices, n, 0, 1, 2)
    
    def func(self, prices, n, day, buy, rem):
        if day == n:
            return 0
        if rem == 0:
            return 0
        if buy:
            buyToday = -prices[day] + self.func(prices, n, day+1, 0, rem)
            skip = self.func(prices, n, day+1, 1, rem)
            return max(buyToday, skip)
        else:
            sellToday = prices[day] + self.func(prices, n, day+1, 1, rem-1)
            skip = self.func(prices, n, day+1, 0, rem)
            return max(sellToday, skip)



class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[[-1] * 3 for _ in range(2)] for _ in range(n)]

        return self.func(prices, n, 0, 1, 2, dp)

    def func(self, prices, n, day, buy, rem, dp):

        if day == n or rem == 0:
            return 0

        if dp[day][buy][rem] != -1:
            return dp[day][buy][rem]

        if buy:
            buyToday = -prices[day] + self.func(prices, n, day + 1, 0, rem, dp)
            skip = self.func(prices, n, day + 1, 1, rem, dp)
            dp[day][buy][rem] = max(buyToday, skip)

        else:
            sellToday = prices[day] + self.func(prices, n, day + 1, 1, rem - 1, dp)
            hold = self.func(prices, n, day + 1, 0, rem, dp)
            dp[day][buy][rem] = max(sellToday, hold)

        return dp[day][buy][rem]


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        for day in range(n - 1, -1, -1):
            for buy in range(2):
                for rem in range(1, 3):

                    if buy:
                        buyToday = -prices[day] + dp[day + 1][0][rem]
                        skip = dp[day + 1][1][rem]
                        dp[day][buy][rem] = max(buyToday, skip)

                    else:
                        sellToday = prices[day] + dp[day + 1][1][rem - 1]
                        hold = dp[day + 1][0][rem]
                        dp[day][buy][rem] = max(sellToday, hold)

        return dp[0][1][2]
