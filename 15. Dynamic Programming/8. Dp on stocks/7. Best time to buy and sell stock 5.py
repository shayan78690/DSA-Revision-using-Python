class Solution(object):
    def maximumProfit(self, prices, k):
        n = len(prices)
        return self.solve(prices, 0, 0, k)

    def solve(self, prices, day, state, k):
        if day == len(prices):
            if state == 0:
                return 0
            return float('-inf')
        if k == 0:
            if state == 0:
                return 0
            return float('-inf')

        # State 0: Nothing in hand
        if state == 0:

            buyNormal = -prices[day] + self.solve(prices, day + 1, 1, k)

            shortSell = prices[day] + self.solve(prices, day + 1, 2, k)

            skip = self.solve(prices, day + 1, 0, k)

            return max(buyNormal, shortSell, skip)

        # State 1: Holding a normal stock
        elif state == 1:

            sellNormal = prices[day] + self.solve(prices, day + 1, 0, k - 1)

            hold = self.solve(prices, day + 1, 1, k)

            return max(sellNormal, hold)

        # State 2: Holding a short position
        else:

            buyBack = -prices[day] + self.solve(prices, day + 1, 0, k - 1)

            wait = self.solve(prices, day + 1, 2, k)

            return max(buyBack, wait)


class Solution(object):
    def maximumProfit(self, prices, k):
        n = len(prices)

        dp = [[[-1] * (k + 1) for _ in range(3)] for _ in range(n)]

        return self.solve(prices, 0, 0, k, dp)

    def solve(self, prices, day, state, k, dp):

        if day == len(prices):
            if state == 0:
                return 0
            return float('-inf')

        if k == 0:
            if state == 0:
                return 0
            return float('-inf')

        if dp[day][state][k] != -1:
            return dp[day][state][k]

        if state == 0:

            buyNormal = -prices[day] + self.solve(prices, day + 1, 1, k, dp)
            shortSell = prices[day] + self.solve(prices, day + 1, 2, k, dp)
            skip = self.solve(prices, day + 1, 0, k, dp)

            dp[day][state][k] = max(buyNormal, shortSell, skip)

        elif state == 1:

            sellNormal = prices[day] + self.solve(prices, day + 1, 0, k - 1, dp)
            hold = self.solve(prices, day + 1, 1, k, dp)

            dp[day][state][k] = max(sellNormal, hold)

        else:

            buyBack = -prices[day] + self.solve(prices, day + 1, 0, k - 1, dp)
            wait = self.solve(prices, day + 1, 2, k, dp)

            dp[day][state][k] = max(buyBack, wait)

        return dp[day][state][k]



class Solution(object):
    def maximumProfit(self, prices, k):
        n = len(prices)

        dp = [[[0] * (k + 1) for _ in range(3)] for _ in range(n + 1)]

        for limit in range(k + 1):
            dp[n][0][limit] = 0
            dp[n][1][limit] = float('-inf')
            dp[n][2][limit] = float('-inf')

        for day in range(n + 1):
            dp[day][0][0] = 0
            dp[day][1][0] = float('-inf')
            dp[day][2][0] = float('-inf')

        for day in range(n - 1, -1, -1):
            for state in range(3):
                for limit in range(1, k + 1):

                    if state == 0:

                        buyNormal = -prices[day] + dp[day + 1][1][limit]
                        shortSell = prices[day] + dp[day + 1][2][limit]
                        skip = dp[day + 1][0][limit]

                        dp[day][state][limit] = max(buyNormal, shortSell, skip)

                    elif state == 1:

                        sellNormal = prices[day] + dp[day + 1][0][limit - 1]
                        hold = dp[day + 1][1][limit]

                        dp[day][state][limit] = max(sellNormal, hold)

                    else:

                        buyBack = -prices[day] + dp[day + 1][0][limit - 1]
                        wait = dp[day + 1][2][limit]

                        dp[day][state][limit] = max(buyBack, wait)

        return dp[0][0][k]
