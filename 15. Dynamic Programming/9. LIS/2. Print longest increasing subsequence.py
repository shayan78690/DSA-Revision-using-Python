class Solution:
    def getLIS(self, arr):
        n = len(arr)
        dp = [1] * n
        parent = [i for i in range(n)]
        maxlen = 1
        lastIndex = 0
        for index in range(n):
            for prevIndex in range(index):
                if arr[index] > arr[prevIndex]:
                    if dp[prevIndex] + 1 > dp[index]:
                        dp[index] = dp[prevIndex] + 1
                        parent[index] = prevIndex
            if dp[index] > maxlen:
                maxlen = dp[index]
                lastIndex = index
            
        result = []
        while parent[lastIndex] != lastIndex:
            result.append(arr[lastIndex])
            lastIndex = parent[lastIndex]
            
        result.append(arr[lastIndex])
        result.reverse()
        return result
