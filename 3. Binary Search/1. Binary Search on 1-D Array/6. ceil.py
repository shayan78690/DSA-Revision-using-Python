#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        ans = -1
        n = len(arr)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
