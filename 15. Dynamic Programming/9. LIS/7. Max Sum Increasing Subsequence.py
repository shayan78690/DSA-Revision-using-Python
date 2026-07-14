class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        return self.solve(arr, 0, -1)

    def solve(self, arr, index, prevIndex):
        if index == len(arr):
            return 0

        skip = self.solve(arr, index + 1, prevIndex)

        take = 0
        if prevIndex == -1 or arr[index] > arr[prevIndex]:
            take = arr[index] + self.solve(arr, index + 1, index)

        return max(skip, take)


class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = [[-1] * (n + 1) for _ in range(n)]
        return self.solve(arr, 0, -1, dp)

    def solve(self, arr, index, prevIndex, dp):
        if index == len(arr):
            return 0

        if dp[index][prevIndex + 1] != -1:
            return dp[index][prevIndex + 1]

        skip = self.solve(arr, index + 1, prevIndex, dp)

        take = 0
        if prevIndex == -1 or arr[index] > arr[prevIndex]:
            take = arr[index] + self.solve(arr, index + 1, index, dp)

        dp[index][prevIndex + 1] = max(skip, take)
        return dp[index][prevIndex + 1]



class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        dp = arr[:]

        maxi = max(arr)

        for index in range(n):
            for prevIndex in range(index):
                if arr[index] > arr[prevIndex]:
                    dp[index] = max(dp[index],
                                    dp[prevIndex] + arr[index])

            maxi = max(maxi, dp[index])

        return maxi








class Solution:
	def maxSumIS(self, arr):
		n = len(arr)
		# dp[i] represent maximum sum of increasing subsequence ending at index i
		dp = arr[:]
		for index in range(n):
		    for prevIndex in range(index):
		        if arr[index] > arr[prevIndex]:
		            dp[index] = max(dp[index], dp[prevIndex] + arr[index])
		return max(dp)
