class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n <= 2:
            return False
        if n == 3:
            if arr[1] > arr[0] and arr[1] > arr[2]:
                return True
        low = 1
        high = n-2
        peak = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                peak = mid
                break
            elif arr[mid] < arr[mid+1]:
                low = mid+1
            else:
                high = mid-1
        
        if peak == -1:
            return False
        for i in range(1, peak+1):
            if arr[i] <= arr[i-1]:
                return False
        for i in range(peak+1, n):
            if arr[i] >= arr[i-1]:
                return False
        return True
        
        
