class Solution:
    def findMaxForm(self, strs, m, n):
        return self.solve(strs, 0, m, n)

    def solve(self, strs, index, zeros, ones):
        if index == len(strs):
            return 0

        currentZeros = strs[index].count('0')
        currentOnes = strs[index].count('1')

        notTake = self.solve(
            strs,
            index + 1,
            zeros,
            ones
        )

        take = 0

        if currentZeros <= zeros and currentOnes <= ones:
            take = 1 + self.solve(
                strs,
                index + 1,
                zeros - currentZeros,
                ones - currentOnes
            )

        return max(take, notTake)


class Solution:
    def findMaxForm(self, strs, m, n):
        dp = [[[-1] * (n + 1) for _ in range(m + 1)] 
              for _ in range(len(strs) + 1)]

        return self.solve(strs, 0, m, n, dp)

    def solve(self, strs, index, zeros, ones, dp):
        if index == len(strs):
            return 0

        if dp[index][zeros][ones] != -1:
            return dp[index][zeros][ones]

        currentZeros = strs[index].count('0')
        currentOnes = strs[index].count('1')

        notTake = self.solve(
            strs, index + 1, zeros, ones, dp
        )

        take = 0

        if currentZeros <= zeros and currentOnes <= ones:
            take = 1 + self.solve(
                strs,
                index + 1,
                zeros - currentZeros,
                ones - currentOnes,
                dp
            )

        dp[index][zeros][ones] = max(take, notTake)

        return dp[index][zeros][ones]


class Solution:
    def findMaxForm(self, strs, m, n):
        length = len(strs)

        dp = [[[0] * (n + 1) for _ in range(m + 1)]
              for _ in range(length + 1)]

        for index in range(length - 1, -1, -1):

            currentZeros = strs[index].count('0')
            currentOnes = strs[index].count('1')

            for zeros in range(m + 1):
                for ones in range(n + 1):

                    notTake = dp[index + 1][zeros][ones]

                    take = 0

                    if currentZeros <= zeros and currentOnes <= ones:
                        take = 1 + dp[index + 1][
                            zeros - currentZeros
                        ][
                            ones - currentOnes
                        ]

                    dp[index][zeros][ones] = max(take, notTake)

        return dp[0][m][n]
