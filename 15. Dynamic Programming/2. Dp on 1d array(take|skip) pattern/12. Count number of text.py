class Solution(object):
    def countTexts(self, pressedKeys):
        n = len(pressedKeys)
        MOD = 10**9+7
        return self.solve(pressedKeys, n, 0, MOD)
    
    def solve(self, s, n, index, MOD):
        if index == n:
            return 1
        
        count = 0
        digit = s[index]
        # Take 1 digit
        count = (count + self.solve(s, n, index+1, MOD)) % MOD
        # Take 2 digits
        if index+1 < n and s[index+1] == digit:
            count = (count + self.solve(s, n, index+2, MOD)) % MOD
        # Take 3 digits
        if index+2 < n:
            if s[index+2] == digit and s[index+1] == digit:
                count = (count + self.solve(s, n, index+3, MOD)) % MOD
        # Take 4 digits
        if digit == "7" or digit == "9": 
            if index+3 < n:
                if s[index+1] == digit and s[index+2] == digit and s[index+3] == digit:
                    count = (count + self.solve(s, n, index+4, MOD)) % MOD
        return count


class Solution(object):
    def countTexts(self, pressedKeys):
        n = len(pressedKeys)
        MOD = 10**9 + 7

        dp = [-1] * n

        return self.solve(pressedKeys, n, 0, MOD, dp)

    def solve(self, s, n, index, MOD, dp):
        if index == n:
            return 1

        if dp[index] != -1:
            return dp[index]

        count = 0
        digit = s[index]

        count += self.solve(s, n, index + 1, MOD, dp)

        if index + 1 < n and s[index + 1] == digit:
            count += self.solve(s, n, index + 2, MOD, dp)

        if index + 2 < n:
            if s[index + 1] == digit and s[index + 2] == digit:
                count += self.solve(s, n, index + 3, MOD, dp)

        if digit == "7" or digit == "9":
            if index + 3 < n:
                if (s[index + 1] == digit and
                    s[index + 2] == digit and
                    s[index + 3] == digit):
                    count += self.solve(s, n, index + 4, MOD, dp)

        dp[index] = count % MOD

        return dp[index]


class Solution(object):
    def countTexts(self, pressedKey):
        n = len(pressedKey)
        MOD = 10**9 + 7
        dp = [0] * (n+1)
        dp[n] = 1
        for index in range(n-1, -1, -1):
            count = 0
            digit = pressedKey[index]
            count += dp[index+1]
            if index+1 < n:
                if pressedKey[index+1] == digit:
                    count += dp[index+2]
            if index+2 < n:
                if pressedKey[index+2] == digit and pressedKey[index+1] == digit:
                    count += dp[index+3]
            if digit == "7" or digit == "9":
                if index+3 < n:
                    if pressedKey[index+1] == digit and pressedKey[index+2] == digit and pressedKey[index+3] == digit:
                        count += dp[index+4]
            dp[index] = count % MOD
        return dp[0]
    
