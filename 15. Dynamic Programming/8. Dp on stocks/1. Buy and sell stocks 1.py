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
        
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        def solve(i, buy):
            if i == n:
                return 0
            if buy == 0:
                skip = solve(i+1, 0)
                take = -prices[i] + solve(i+1, 1)
                return max(take, skip)
            else:
                skip = solve(i+1, 1)
                take = prices[i]
                return max(take, skip)
        return solve(0, 0)
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for buy in range(2):
                if buy == 0:
                    skip = dp[i+1][0]
                    take = -prices[i] + dp[i+1][1]
                    dp[i][buy] = max(take, skip)
                else:
                    skip = dp[i+1][1]
                    take = prices[i]
                    dp[i][buy] = max(take, skip)
        return dp[0][0]
