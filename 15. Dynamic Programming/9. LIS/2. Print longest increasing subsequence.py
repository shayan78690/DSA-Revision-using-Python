class Solution:
    def getLIS(self, arr):
        n = len(arr)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for index in range(n-1, -1, -1):
            for prevIndex in range(index-1, -2, -1):
                skip = dp[index+1][prevIndex+1]
                take = 0
                if prevIndex == -1 or arr[index] > arr[prevIndex]:
                    take = 1 + dp[index+1][index+1]
                dp[index][prevIndex+1] = max(take, skip)
        
        index = 0
        prevIndex = -1
        result = []
        while index < n:
            skip = dp[index+1][prevIndex+1]
            take = 0
            if prevIndex == -1 or arr[index] > arr[prevIndex]:
                take = 1 + dp[index+1][index+1]
            
            if take >= skip and (prevIndex == -1 or arr[index] > arr[prevIndex]):
                result.append(arr[index])
                prevIndex = index
                
            index += 1
        
        return result
