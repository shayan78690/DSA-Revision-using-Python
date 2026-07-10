class Solution:
    def knapSack(self, val, wt, capacity):
        return self.func(val, wt, 0, capacity)
    
    def func(self, val, wt, index, capacity):
        if capacity == 0 or index == len(wt):
            return 0
        notTake = self.func(
            val,
            wt,
            index + 1,
            capacity
        )
        take = 0
        if wt[index] <= capacity:
            take = val[index] + self.func(
                val,
                wt,
                index,
                capacity - wt[index]
            )
        return max(take, notTake)


class Solution:

    def knapSack(self, val, wt, capacity):

        n = len(wt)
        dp = [[-1] * (capacity + 1) for _ in range(n + 1)]

        return self.func(val, wt, 0, capacity, dp)

    def func(self, val, wt, index, capacity, dp):

        if capacity == 0 or index == len(wt):
            return 0

        if dp[index][capacity] != -1:
            return dp[index][capacity]

        notTake = self.func(
            val,
            wt,
            index + 1,
            capacity,
            dp
        )

        take = 0

        if wt[index] <= capacity:
            take = val[index] + self.func(
                val,
                wt,
                index,
                capacity - wt[index],
                dp
            )

        dp[index][capacity] = max(take, notTake)
        return dp[index][capacity]



class Solution:

    def knapSack(self, val, wt, capacity):

        n = len(wt)

        dp = [[0] * (capacity + 1) for _ in range(n + 1)]

        for index in range(n - 1, -1, -1):

            for cap in range(capacity + 1):

                notTake = dp[index + 1][cap]

                take = 0

                if wt[index] <= cap:
                    take = val[index] + dp[index][cap - wt[index]]

                dp[index][cap] = max(take, notTake)

        return dp[0][capacity]
