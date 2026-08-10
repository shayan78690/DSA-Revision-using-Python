class Solution:
	def perfectSum(self, arr, target):
		n = len(arr)
		dp = [[-1] * (target+1) for _ in range(n+1)]
		return self.solve(arr, n, target, 0, 0, dp)
	
	def solve(self, arr, n, target, index, current_sum, dp):
	    if index == n:
	        return 1 if current_sum == target else 0
	    if dp[index][current_sum] != -1:
	        return dp[index][current_sum]
	    skip = self.solve(arr, n, target, index+1, current_sum, dp)
	    take = 0
	    if arr[index] + current_sum <= target:
	        take = self.solve(arr, n, target, index+1, arr[index]+current_sum, dp)
	        
	    dp[index][current_sum] = take + skip
	    return dp[index][current_sum]


class Solution:
	def perfectSum(self, arr, target):
		n = len(arr)
		dp = [[0] * (target+1) for _ in range(n+1)]
		dp[n][target] = 1
		for index in range(n-1, -1, -1):
		    for current_sum in range(target+1):
		        count = dp[index+1][current_sum]
		        if arr[index] + current_sum <= target:
		            count += dp[index+1][current_sum+arr[index]]
		        dp[index][current_sum] = count
		return dp[0][0]
	
