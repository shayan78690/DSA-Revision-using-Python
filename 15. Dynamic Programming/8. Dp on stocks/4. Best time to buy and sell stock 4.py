class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)
        dp = [[[-1] * (k + 1) for _ in range(2)] for _ in range(n)]
        return self.solve(prices, 0, 1, k, dp)

    def solve(self, prices, day, buy, limit, dp):

        if day == len(prices):
            return 0

        if limit == 0:
            return 0

        if dp[day][buy][limit] != -1:
            return dp[day][buy][limit]

        if buy:
            buyToday = -prices[day] + self.solve(prices, day + 1, 0, limit, dp)
            skip = self.solve(prices, day + 1, 1, limit, dp)
            dp[day][buy][limit] = max(buyToday, skip)
        else:
            sellToday = prices[day] + self.solve(prices, day + 1, 1, limit - 1, dp)
            hold = self.solve(prices, day + 1, 0, limit, dp)
            dp[day][buy][limit] = max(sellToday, hold)

        return dp[day][buy][limit]


class Solution:
    def maxProfit(self, k, prices):
        n = len(prices)

        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]

        for day in range(n - 1, -1, -1):
            for buy in range(2):
                for limit in range(1, k + 1):

                    if buy:
                        buyToday = -prices[day] + dp[day + 1][0][limit]
                        skip = dp[day + 1][1][limit]
                        dp[day][buy][limit] = max(buyToday, skip)

                    else:
                        sellToday = prices[day] + dp[day + 1][1][limit - 1]
                        hold = dp[day + 1][0][limit]
                        dp[day][buy][limit] = max(sellToday, hold)

        return dp[0][1][k]
