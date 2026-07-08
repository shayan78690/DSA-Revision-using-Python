class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        return self.func(questions, n, 0)
    
    def func(self, nums, n, index):
        if index >= n:
            return 0
        points, skip = nums[index]
        take = points + self.func(nums, n, index+skip+1)
        notTake =self.func(nums, n, index+1)
        return max(take, notTake)



class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [-1] * n
        return self.func(questions, n, 0, dp)
    
    def func(self, nums, n, index, dp):
        if index >= n:
            return 0
        if dp[index] != -1:
            return dp[index]
        points, skip = nums[index]
        take = points + self.func(nums, n, index+skip+1, dp)
        notTake =self.func(nums, n, index+1, dp)
        dp[index] = max(take, notTake)
        return dp[index]



class Solution(object):
    def mostPoints(self, questions):
        n = len(questions)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            points, skip = questions[i]
            take = points
            if i+skip+1 < n:
               take += dp[i+skip+1]
            notTake = dp[i+1]
            dp[i] = max(take, notTake)
        return dp[0]
     
