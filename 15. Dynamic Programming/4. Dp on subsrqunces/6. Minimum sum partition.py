class Solution:
	def minDifference(self, arr):
		n = len(arr)
		total = sum(arr)
		# total = S
		# s1 = x
		# s2 = S-x
		# we want (S-x)-x to be minimum
		return self.func(arr, n, total, 0, 0)
	
	def func(self, arr, n, total, index, current_sum):
	    if index == n:
	        sum1 = current_sum
	        sum2 = total - current_sum
	        return abs(sum2-sum1)
	    
	    take = self.func(arr, n, total, index+1, current_sum+arr[index])
	    skip = self.func(arr, n, total, index+1, current_sum)
	    
	    return min(take, skip)


class Solution:
	def minDifference(self, arr):
		n = len(arr)
		total = sum(arr)
		# total = S
		# s1 = x
		# s2 = S-x
		# we want (S-x)-x to be minimum
		return self.func(arr, n, total, 0, 0)
	
	def func(self, arr, n, total, index, current_sum):
	    if index == n:
	       # sum1 = current_sum
	       # sum2 = total - current_sum
	        return abs(total-2*current_sum)
	    
	    take = self.func(arr, n, total, index+1, current_sum+arr[index])
	    skip = self.func(arr, n, total, index+1, current_sum)
	    
	    return min(take, skip)



class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        n = len(arr)
        dp = [[-1] * (total + 1) for _ in range(n)]
        return self.func(arr, 0, 0, total, n, dp)

    def func(self, arr, index, currentSum, total, n, dp):
        if index == n:
            return abs(total - 2 * currentSum)
        if dp[index][currentSum] != -1:
            return dp[index][currentSum]
        take = self.func(
            arr,
            index + 1,
            currentSum + arr[index],
            total,
            n,
            dp
        )
        notTake = self.func(
            arr,
            index + 1,
            currentSum,
            total,
            n,
            dp
        )
        dp[index][currentSum] = min(take, notTake)
        return dp[index][currentSum]



class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        n = len(arr)

        dp = [[0] * (total + 1) for _ in range(n + 1)]

        for currentSum in range(total + 1):
            dp[n][currentSum] = abs(total - 2 * currentSum)

        for index in range(n - 1, -1, -1):
            for currentSum in range(total, -1, -1):

                take = float('inf')
                if currentSum + arr[index] <= total:
                    take = dp[index + 1][currentSum + arr[index]]

                notTake = dp[index + 1][currentSum]

                dp[index][currentSum] = min(take, notTake)

        return dp[0][0]





