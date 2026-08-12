class Solution(object):
    def longestObstacleCourseAtEachPosition(self, arr):
        n = len(arr)
        dp = [1] * n
        for index in range(n):
            for prev in range(index):
                if arr[index] >= arr[prev]:
                    dp[index] = max(dp[index], dp[prev]+1)
        return dp





class Solution(object):
    def longestObstacleCourseAtEachPosition(self, arr):
        result = []
        tail = []

        for x in arr:
            low = 0
            high = len(tail) - 1
            while low <= high:
                mid = (low + high) // 2
                if tail[mid] > x:
                    high = mid-1
                else:
                    low = mid + 1
            pos = low
            if pos == len(tail):
                tail.append(x)
            else:
                tail[pos] = x

            result.append(pos + 1)

        return result
