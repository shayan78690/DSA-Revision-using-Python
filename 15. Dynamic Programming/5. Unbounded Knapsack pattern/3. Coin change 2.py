class Solution:
    def change(self, amount, coins):
        return self.func(coins, 0, amount)

    def func(self, coins, index, amount):
        if amount == 0:
            return 1
        if index == len(coins):
            return 0
        notTake = self.func(
            coins,
            index + 1,
            amount
        )
        take = 0
        if coins[index] <= amount:
            take = self.func(
                coins,
                index,
                amount - coins[index]
            )
        return take + notTake



class Solution:

    def change(self, amount, coins):

        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]

        return self.func(coins, 0, amount, dp)

    def func(self, coins, index, amount, dp):

        if amount == 0:
            return 1

        if index == len(coins):
            return 0

        if dp[index][amount] != -1:
            return dp[index][amount]

        notTake = self.func(
            coins,
            index + 1,
            amount,
            dp
        )

        take = 0

        if coins[index] <= amount:
            take = self.func(
                coins,
                index,
                amount - coins[index],
                dp
            )

        dp[index][amount] = take + notTake
        return dp[index][amount]



class Solution:

    def change(self, amount, coins):

        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for index in range(n+1):
            dp[index][0] = 1

        for index in range(n - 1, -1, -1):
            for amt in range(1, amount + 1):
                notTake = dp[index + 1][amt]
                take = 0
                if coins[index] <= amt:
                    take = dp[index][amt - coins[index]]
                dp[index][amt] = take + notTake

        return dp[0][amount]

