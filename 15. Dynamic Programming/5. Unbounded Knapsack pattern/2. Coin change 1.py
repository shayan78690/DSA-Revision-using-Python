class Solution:

    def coinChange(self, coins, amount):

        ans = self.func(coins, 0, amount)

        if ans == float('inf'):
            return -1

        return ans

    def func(self, coins, index, amount):

        if amount == 0:
            return 0

        if index == len(coins):
            return float('inf')

        notTake = self.func(coins, index + 1, amount)

        take = float('inf')

        if coins[index] <= amount:
            take = 1 + self.func(
                coins,
                index,
                amount - coins[index]
            )

        return min(take, notTake)



class Solution:

    def coinChange(self, coins, amount):

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        ans = self.func(coins, 0, amount, dp)

        if ans == float('inf'):
            return -1

        return ans

    def func(self, coins, index, amount, dp):

        if amount == 0:
            return 0

        if index == len(coins):
            return float('inf')

        if dp[index][amount] != -1:
            return dp[index][amount]

        notTake = self.func(coins, index + 1, amount, dp)

        take = float('inf')

        if coins[index] <= amount:
            take = 1 + self.func(
                coins,
                index,
                amount - coins[index],
                dp
            )

        dp[index][amount] = min(take, notTake)
        return dp[index][amount]



class Solution:

    def coinChange(self, coins, amount):

        n = len(coins)

        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        dp[n][0] = 0

        for index in range(n - 1, -1, -1):
            dp[index][0] = 0

            for amt in range(1, amount + 1):

                notTake = dp[index + 1][amt]

                take = float('inf')

                if coins[index] <= amt:
                    take = 1 + dp[index][amt - coins[index]]

                dp[index][amt] = min(take, notTake)

        if dp[0][amount] == float('inf'):
            return -1

        return dp[0][amount]
