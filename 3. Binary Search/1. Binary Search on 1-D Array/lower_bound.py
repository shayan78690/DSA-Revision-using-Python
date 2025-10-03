class Solution:
    def lowerBound(self, arr, target):
        index = len(arr)
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= target:
                index = mid
                high = mid - 1
            else:
                low = mid + 1
        return index