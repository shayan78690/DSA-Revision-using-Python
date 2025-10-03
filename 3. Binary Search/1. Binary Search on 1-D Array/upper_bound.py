class Solution:
    def upperBound(self, arr, target):
        n = len(arr)
        low = 0
        high = n-1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans
        