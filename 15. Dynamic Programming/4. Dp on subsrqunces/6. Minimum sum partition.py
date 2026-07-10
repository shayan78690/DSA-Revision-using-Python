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
		dp = [[-1] * (total+1) for _ in range(n)]
		return self.func(arr, n, total, 0, 0, dp)
	
	def func(self, arr, n, total, index, current_sum, dp):
	    if index == n:
	        sum1 = current_sum
	        sum2 = total - current_sum
	        return abs(sum2-sum1)
	   
	    if dp[index][current_sum] != -1:
	        return dp[index][current_sum]
	    
	    take = self.func(arr, n, total, index+1, current_sum+arr[index], dp)
	    skip = self.func(arr, n, total, index+1, current_sum, dp)
	    
	    dp[index][current_sum] = min(take, skip)
	    return dp[index][current_sum]


