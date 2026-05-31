class Solution:
    def maxSum(self, arr):
        maxi = float('-inf')
        if len(arr) < 2:
            return 0
        for i in range(len(arr)-1):
            s = arr[i] + arr[i+1]
            maxi = max(maxi, s)
        return maxi
            
    
