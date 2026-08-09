class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        return self.func(mat, n, 0, 3)
    
    def func(self, mat, n, day, last):
        if day == n:
            return 0
        
        first = 0
        if last != 0:
            first = max(first, mat[day][0] + self.func(mat, n, day+1, 0))
        
        second = 0
        if last != 1:
            second = max(second, mat[day][1] + self.func(mat, n, day+1, 1))
        
        third = 0
        if last != 2:
            third = max(third, mat[day][2] + self.func(mat, n, day+1, 2))
        
        return max(first, second, third)
        


class Solution:
    def ninjaTraining(self, n, points):
        return self.func(0, 3, points, n)

    def func(self, day, last, points, n):

        if day == n:
            return 0

        maxi = 0

        for task in range(3):
            if task != last:
                score = points[day][task] + self.func(day + 1, task, points, n)
                maxi = max(maxi, score)

        return maxi





class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        dp = [[-1] * 4 for _ in range(n)]
        return self.func(mat, n, 0, 3, dp)
    
    def func(self, mat, n, day, last, dp):
        if day == n:
            return 0
        if dp[day][last] != -1:
            return dp[day][last]
        
        first = 0
        if last != 0:
            first = max(first, mat[day][0] + self.func(mat, n, day+1, 0, dp))
        
        second = 0
        if last != 1:
            second = max(second, mat[day][1] + self.func(mat, n, day+1, 1, dp))
        
        third = 0
        if last != 2:
            third = max(third, mat[day][2] + self.func(mat, n, day+1, 2, dp))
        
        dp[day][last] = max(first, second, third)
        return dp[day][last]


class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        dp = [[0] * 4 for _ in range(n+1)]
        
        for day in range(n-1, -1, -1):
            for last in range(4):
                first = 0
                if last != 0:
                    first = mat[day][0] + dp[day+1][0]
        
                second = 0
                if last != 1:
                    second = mat[day][1] + dp[day+1][1]
        
                third = 0
                if last != 2:
                    third = mat[day][2] + dp[day+1][2]
        
                dp[day][last] = max(first, second, third)
        
        return dp[0][3]



class Solution:
    def maximumPoints(self, mat):
        n = len(mat)
        dp = [[0] * 4 for _ in range(n+1)]
        
        for day in range(n-1, -1, -1):
            for last in range(4):
                maxi = 0
                for task in range(3):
                    if task != last:
                        points = dp[day+1][task] + mat[day][task]
                        maxi = max(maxi, points)
                dp[day][last] = maxi
        return dp[0][3]
