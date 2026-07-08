class Solution(object):
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums)+1)
        for num in nums:
            points[num] += num
        return self.func(points, 0)

    def func(self, points, index):
        if index >= len(points):
            return 0
        take = points[index] + self.func(points, index+2)
        skip = self.func(points, index+1)
        return max(take, skip)
        


class Solution(object):
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums)+1)
        for num in nums:
            points[num] += num
        dp = [-1] * len(points)
        return self.func(points, 0, dp)

    def func(self, points, index, dp):
        if index >= len(points):
            return 0
        if dp[index] != -1:
            return dp[index]
        take = points[index] + self.func(points, index+2, dp)
        skip = self.func(points, index+1, dp)
        dp[index] = max(take, skip)
        return dp[index]
        




class Solution(object):
    def deleteAndEarn(self, nums):
        points = [0] * (max(nums)+1)
        for num in nums:
            points[num] += num
        dp = [0] * (len(points)+2)
        for i in range(len(points)-1, -1, -1):
            take = points[i] + dp[i+2]
            skip = dp[i+1]
            dp[i] = max(take, skip)
        return dp[0]

   
        
        
