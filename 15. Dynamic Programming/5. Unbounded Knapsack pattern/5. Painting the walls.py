class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = [[-1] * (n+1) for _ in range(n+1)]
        return self.solve(cost, time, n, 0, 0, dp)
    
    def solve(self, cost, time, n, index, current_painted_walls, dp):
        if current_painted_walls >= n:
            return 0
        if index == n:
            return float('inf')
        
        if dp[index][current_painted_walls] != -1:
            return dp[index][current_painted_walls]

        paint = cost[index] + self.solve(cost, time, n, index+1, current_painted_walls+time[index]+1, dp)
        not_paint = self.solve(cost, time, n, index+1, current_painted_walls, dp)        
        dp[index][current_painted_walls] = min(paint, not_paint)
        return dp[index][current_painted_walls]



class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        for current_painted_walls in range(n+1):
            dp[n][current_painted_walls] = 0 if current_painted_walls >= n else float('inf')
        for index in range(n-1, -1, -1):
            for current in range(n+1):
                if current >= n:
                    dp[index][current] = 0
                    continue
                paint = cost[index] + dp[index+1][min(current+time[index]+1, n)]
                not_paint = dp[index+1][current]
                dp[index][current] = min(paint, not_paint)
        return dp[0][0]

