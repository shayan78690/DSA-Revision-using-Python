class Solution(object):
    def mincostTickets(self, days, costs):
        n = len(days)
        
        return self.func(days, costs, n, 0)
    
    def func(self, days, costs, n, i):
        if i >= n:
            return 0
        j = i
        while j < n and days[j] < days[i]+1:
            j += 1
        one = costs[0] + self.func(days, costs, n, j)

        j = i
        while j < n and days[j] < days[i]+7:
            j += 1
        seven = costs[1] + self.func(days, costs, n, j)

        j = i
        while j < n and days[j] < days[i]+30:
            j += 1
        thirty = costs[2] + self.func(days, costs, n, j)

        return min(one, seven, thirty)



class Solution(object):
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [-1] * n
        return self.func(days, costs, n, 0, dp)
    
    def func(self, days, costs, n, i, dp):
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]
        j = i
        while j < n and days[j] < days[i]+1:
            j += 1
        one = costs[0] + self.func(days, costs, n, j, dp)

        j = i
        while j < n and days[j] < days[i]+7:
            j += 1
        seven = costs[1] + self.func(days, costs, n, j, dp)

        j = i
        while j < n and days[j] < days[i]+30:
            j += 1
        thirty = costs[2] + self.func(days, costs, n, j, dp)

        dp[i] = min(one, seven, thirty)
        return dp[i]



class Solution(object):
    def mincostTickets(self, days, costs):
        n = len(days)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            j = i
            while j < n and days[j] < days[i]+1:
                j += 1
            one = costs[0] + dp[j] 

            j = i
            while j < n and days[j] < days[i]+7:
                j += 1
            seven = costs[1] + dp[j]

            j = i
            while j < n and days[j] < days[i]+30:
                j += 1
            thirty = costs[2] + dp[j]

            dp[i] = min(one, seven, thirty)
        return dp[0]
    
    
