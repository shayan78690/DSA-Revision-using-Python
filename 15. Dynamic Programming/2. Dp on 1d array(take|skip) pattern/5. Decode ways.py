class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        return self.func(s, n, 0)
        
    def func(self, s, n, index):
        if index == n:
            return 1
        if s[index] == '0':
            return 0
        take_one = self.func(s, n, index+1)
        take_two = 0
        if index+1 < n and 10 <= int(s[index:index+2]) <= 26:
            take_two = self.func(s, n, index+2)
        return take_one + take_two


class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [-1] * n
        return self.func(s, n, 0, dp)
        
    def func(self, s, n, index, dp):
        if index == n:
            return 1
        if s[index] == '0':
            return 0
        if dp[index] != -1:
            return dp[index]
        take_one = self.func(s, n, index+1, dp)
        take_two = 0
        if index+1 < n and 10 <= int(s[index:index+2]) <= 26:
            take_two = self.func(s, n, index+2, dp)
        dp[index] = take_one + take_two
        return dp[index]


class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        dp = [0] * (n+1)
        dp[n] = 1
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            take_one = dp[i+1]
            take_two = 0
            if i+1 < n and 10 <= int(s[i:i+2]) <= 26:
                take_two = dp[i+2]
            dp[i] = take_one + take_two
        return dp[0]
