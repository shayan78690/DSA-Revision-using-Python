class Solution:

    def cutRod(self, price):
        n = len(price)

        return self.func(price, 0, n)

    def func(self, price, index, remaining):

        if remaining == 0:
            return 0

        if index == len(price):
            return 0

        pieceLength = index + 1

        notTake = self.func(
            price,
            index + 1,
            remaining
        )

        take = 0

        if pieceLength <= remaining:
            take = price[index] + self.func(
                price,
                index,
                remaining - pieceLength
            )

        return max(take, notTake)




class Solution:

    def cutRod(self, price):
        n = len(price)
        dp = [[-1] * (n + 1) for _ in range(n)]

        return self.func(price, 0, n, dp)

    def func(self, price, index, remaining, dp):

        if remaining == 0:
            return 0

        if index == len(price):
            return 0

        if dp[index][remaining] != -1:
            return dp[index][remaining]

        pieceLength = index + 1

        notTake = self.func(
            price,
            index + 1,
            remaining,
            dp
        )

        take = 0

        if pieceLength <= remaining:
            take = price[index] + self.func(
                price,
                index,
                remaining - pieceLength,
                dp
            )

        dp[index][remaining] = max(take, notTake)

        return dp[index][remaining]



class Solution:
    def cutRod(self, price: list[int]) -> int:
        n = len(price)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for index in range(n-1, -1, -1):
            piece_length = index+1
            for remaining in range(n+1):
                not_cut = dp[index+1][remaining]
                cut = 0
                if piece_length <= remaining:
                    cut = dp[index][remaining-piece_length] + price[index]
                dp[index][remaining] = max(cut, not_cut)
        return dp[0][n]
