class Solution:
    def maxSum(self, arr):
        maxi = float('-inf')
        if len(arr) < 2:
            return 0
        for i in range(len(arr)-1):
            s = arr[i] + arr[i+1]
            maxi = max(maxi, s)
        return maxi
            
    
class Solution:
    def maxSum(self, arr):
        n = len(arr)
        left = 0
        right = 0
        maxi = 0
        s = 0
        while right < n:
            s += arr[right]
            if right-left+1 > 2:
                s -= arr[left]
                left += 1
            if right-left+1 == 2:
                maxi = max(maxi, s)
            right += 1
        return maxi
    
