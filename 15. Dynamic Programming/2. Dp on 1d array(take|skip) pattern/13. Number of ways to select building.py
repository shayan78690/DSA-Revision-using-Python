class Solution(object):
    def numberOfWays(self, s):
        n = len(s)
        return self.solve(s, n, 0, "", 0)
    
    def solve(self, s, n, index, prev, count):
        if count == 3:
            return 1
        if index == n:
            return 0
        # skip building 
        skip = self.solve(s, n, index+1, prev, count)
        # take building
        take = 0
        if prev == "" or s[index] != prev:
            take = self.solve(s, n, index+1, s[index], count+1)
        return take + skip




class Solution(object):
    def numberOfWays(self, s):
        n = len(s)
        dp = [[[-1] * 4 for _ in range(2)] for _ in range(n+1)]
        return self.solve(s, n, 0, 0, 0, dp)
    
    def solve(self, s, n, index, prev, count, dp):
        if count == 3:
            return 1
        if index == n:
            return 0
        if dp[index][prev][count] != -1:
            return dp[index][prev][count]
        skip = self.solve(s, n, index+1, prev, count, dp)
        take = 0
        if count == 0 or int(s[index]) != prev:
            take = self.solve(s, n, index+1, int(s[index]), count+1, dp)
        dp[index][prev][count] = take + skip
        return dp[index][prev][count]




class Solution(object):
    def numberOfWays(self, s):
        n = len(s)
        dp = [[[0] * 4 for _ in range(3)] for _ in range(n+1)]
        for index in range(n+1):
            for prev in range(3):
                dp[index][prev][3] = 1
        for index in range(n-1, -1, -1):
            for prev in range(3):
                for count in range(3):
                    skip = dp[index+1][prev][count]
                    take = 0
                    if prev == 2 or prev != int(s[index]):
                        take = dp[index+1][int(s[index])][count+1]
                    dp[index][prev][count] = take + skip
        return dp[0][2][0]





