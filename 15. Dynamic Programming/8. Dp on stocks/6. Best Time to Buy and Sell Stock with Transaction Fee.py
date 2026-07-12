class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        return self.solve(prices, fee, 0, 1, dp)

    def solve(self, prices, fee, day, buy, dp):

        if day == len(prices):
            return 0

        if dp[day][buy] != -1:
            return dp[day][buy]

        if buy:
            buyToday = -prices[day] + self.solve(prices, fee, day + 1, 0, dp)
            skip = self.solve(prices, fee, day + 1, 1, dp)
            dp[day][buy] = max(buyToday, skip)
        else:
            sellToday = prices[day] - fee + self.solve(prices, fee, day + 1, 1, dp)
            hold = self.solve(prices, fee, day + 1, 0, dp)
            dp[day][buy] = max(sellToday, hold)

        return dp[day][buy]


class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)

        dp = [[0] * 2 for _ in range(n + 1)]

        for day in range(n - 1, -1, -1):
            for buy in range(2):

                if buy:
                    buyToday = -prices[day] + dp[day + 1][0]
                    skip = dp[day + 1][1]
                    dp[day][buy] = max(buyToday, skip)

                else:
                    sellToday = prices[day] - fee + dp[day + 1][1]
                    hold = dp[day + 1][0]
                    dp[day][buy] = max(sellToday, hold)

        return dp[0][1]
