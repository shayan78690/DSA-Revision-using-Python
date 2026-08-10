class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9+7
        dp = [[[-1] * (sum(profit)+1) for _ in range(n+1)] for _ in range(len(group)+1)]
        return self.solve(n, minProfit, group, profit, 0, 0, 0, dp, MOD)
    
    def solve(self, n, minProfit, group, profit, index, people_used, profit_earned, dp, MOD):
        if people_used > n:
            return 0
        if index == len(group):
            if profit_earned >= minProfit and people_used <= n:
                return 1
            return 0
        if dp[index][people_used][profit_earned] != -1:
            return dp[index][people_used][profit_earned]
        count = 0 
        count = (count + self.solve(n, minProfit, group, profit, index+1, people_used, profit_earned, dp, MOD)) % MOD
        if people_used+group[index] <= n:
            count = (count + self.solve(n, minProfit, group, profit, index+1, people_used+group[index], profit_earned+profit[index], dp, MOD)) % MOD
        dp[index][people_used][profit_earned] = count
        return dp[index][people_used][profit_earned] 



class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7
        return self.solve(
            n, minProfit, group, profit,
            0, 0, 0, MOD
        )

    def solve(self, n, minProfit, group, profit,
              index, people_used, profit_earned, MOD):

        if people_used > n:
            return 0

        if index == len(group):
            if profit_earned >= minProfit:
                return 1
            return 0

        profit_earned = min(profit_earned, minProfit)

        skip = self.solve(
            n, minProfit, group, profit,
            index + 1,
            people_used,
            profit_earned,
            MOD
        )

        take = 0

        if people_used + group[index] <= n:
            take = self.solve(
                n, minProfit, group, profit,
                index + 1,
                people_used + group[index],
                min(profit_earned + profit[index], minProfit),
                MOD
            )

        return (skip + take) % MOD






                class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7

        dp = [
            [[-1] * (minProfit + 1) for _ in range(n + 1)]
            for _ in range(len(group) + 1)
        ]

        return self.solve(
            n, minProfit, group, profit,
            0, 0, 0, dp, MOD
        )

    def solve(self, n, minProfit, group, profit,
              index, people_used, profit_earned, dp, MOD):

        if people_used > n:
            return 0

        if index == len(group):
            if profit_earned >= minProfit:
                return 1
            return 0

        profit_earned = min(profit_earned, minProfit)

        if dp[index][people_used][profit_earned] != -1:
            return dp[index][people_used][profit_earned]

        skip = self.solve(
            n, minProfit, group, profit,
            index + 1,
            people_used,
            profit_earned,
            dp, MOD
        )

        take = 0

        if people_used + group[index] <= n:
            take = self.solve(
                n, minProfit, group, profit,
                index + 1,
                people_used + group[index],
                min(profit_earned + profit[index], minProfit),
                dp, MOD
            )

        dp[index][people_used][profit_earned] = (
            skip + take
        ) % MOD

        return dp[index][people_used][profit_earned]




class Solution(object):
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7
        m = len(group)
        dp = [[[0] * (minProfit + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for people_used in range(n + 1):
            dp[m][people_used][minProfit] = 1

        for index in range(m - 1, -1, -1):
            for people_used in range(n + 1):
                for profit_earned in range(minProfit + 1):
                    skip = dp[index + 1][people_used][profit_earned]
                    take = 0
                    if people_used + group[index] <= n:
                        new_profit = min(profit_earned + profit[index], minProfit)
                        take = dp[index + 1][people_used + group[index]][new_profit]

                    dp[index][people_used][profit_earned] = (skip + take) % MOD

        return dp[0][0][0]
                
