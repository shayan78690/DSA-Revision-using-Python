class Solution:
    def countPartitions(self, arr, diff):
        n = len(arr)
        total = sum(arr)
        dp = [[-1] * (total+1) for _ in range(n+1)]
        return self.solve(arr, n, diff, total, 0, 0, dp)

    def solve(self, arr, n, diff, total, index, subset1, dp):
        if index == n:
            subset2 = total - subset1
            if subset1 - subset2 == diff:
                return 1
            return 0
        if dp[index][subset1] != -1:
            return dp[index][subset1]
        skip = self.solve(
            arr, n, diff, total,
            index + 1,
            subset1,
            dp
        )
        take = self.solve(
            arr, n, diff, total,
            index + 1,
            subset1 + arr[index],
            dp
        )
        dp[index][subset1] = take + skip
        return dp[index][subset1]


class Solution:
    def countPartitions(self, arr, diff):
        n = len(arr)
        total = sum(arr)
        dp = [[0] * (total+1) for _ in range(n+1)]
        for subset1 in range(total+1):
            subset2 = total - subset1
            if subset1 - subset2 == diff:
                dp[n][subset1] = 1
                
        for index in range(n-1, -1, -1):
            for subset1 in range(total+1):
                skip = dp[index+1][subset1]
                take = 0
                if arr[index] + subset1 <= total:
                    take = dp[index+1][subset1+arr[index]]
                dp[index][subset1] = take + skip
        return dp[0][0]





class Solution:

    def countPartitions(self, arr, diff):
        total = sum(arr)
        if total < diff:
            return 0
        # s1+s2 = total
        # s1-s2 = d
        # 2*s1 = total+d
        # s1 = (total+d)//2
        # s2 = (total-d)//2
        # target = (total-d) // 2
        if (total - diff) % 2 != 0:
            return 0
        target = (total - diff) // 2
        return self.func(arr, 0, target)

    def func(self, arr, index, target):

        if index == len(arr):
            if target == 0:
                return 1
            return 0

        notTake = self.func(arr, index + 1, target)

        take = 0

        if arr[index] <= target:
            take = self.func(arr,
                             index + 1,
                             target - arr[index])

        return take + notTake



class Solution:

    def countPartitions(self, arr, diff):
        total = sum(arr)
        if total < diff:
            return 0
        if (total - diff) % 2 != 0:
            return 0
        target = (total - diff) // 2
        n = len(arr)
        dp = [[-1] * (target + 1) for _ in range(n)]

        return self.func(arr, 0, target, dp)

    def func(self, arr, index, target, dp):

        if index == len(arr):
            if target == 0:
                return 1
            return 0

        if dp[index][target] != -1:
            return dp[index][target]

        notTake = self.func(arr, index + 1, target, dp)

        take = 0
        if arr[index] <= target:
            take = self.func(arr, index + 1, target - arr[index], dp)

        dp[index][target] = take + notTake
        return dp[index][target]



class Solution:

    def countPartitions(self, arr, diff):
        total = sum(arr)

        if total < diff:
            return 0

        if (total - diff) % 2 != 0:
            return 0

        target = (total - diff) // 2
        n = len(arr)

        dp = [[0] * (target + 1) for _ in range(n + 1)]

        # Base case
        dp[n][0] = 1

        for index in range(n - 1, -1, -1):
            for t in range(target + 1):

                notTake = dp[index + 1][t]

                take = 0
                if arr[index] <= t:
                    take = dp[index + 1][t - arr[index]]

                dp[index][t] = take + notTake

        return dp[0][target]



