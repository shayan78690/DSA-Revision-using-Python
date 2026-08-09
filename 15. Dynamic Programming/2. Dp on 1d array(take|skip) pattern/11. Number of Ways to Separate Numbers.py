class Solution(object):
    def numberOfCombinations(self, num):
        n = len(num)
        MOD = 10**9 + 7

        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        return self.solve(num, n, 0, "", MOD, dp)

    def solve(self, s, n, index, prev, MOD, dp):

        if index == n:
            return 1

        if s[index] == "0":
            return 0

        if prev == "":
            prev_index = n
        else:
            prev_index = index - len(prev)

        if dp[index][prev_index] != -1:
            return dp[index][prev_index]

        count = 0

        for end in range(index, n):

            current = s[index:end + 1]

            if prev == "" or self.isValid(current, prev):

                count = (
                    count +
                    self.solve(
                        s,
                        n,
                        end + 1,
                        current,
                        MOD,
                        dp
                    )
                ) % MOD

        dp[index][prev_index] = count

        return count

    def isValid(self, current, prev):

        if len(current) > len(prev):
            return True

        if len(prev) > len(current):
            return False

        return current >= prev




class Solution(object):
    def numberOfCombinations(self, num):
        n = len(num)
        MOD = 10**9 + 7

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for prev_start in range(n + 1):
            dp[n][prev_start] = 1

        for index in range(n - 1, -1, -1):

            if num[index] == "0":
                continue

            for prev_start in range(n + 1):

                if prev_start == n:
                    prev = ""
                else:
                    prev = num[prev_start:index]

                count = 0

                for end in range(index, n):

                    current = num[index:end + 1]

                    if prev == "" or self.isValid(current, prev):
                        count = (count + dp[end + 1][index]) % MOD

                dp[index][prev_start] = count

        return dp[0][n]

    def isValid(self, current, prev):

        if len(current) > len(prev):
            return True

        if len(prev) > len(current):
            return False

        return current >= prev
