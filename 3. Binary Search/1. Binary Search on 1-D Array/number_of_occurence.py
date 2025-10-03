class Solution:
    def first(self, arr, target):
        n = len(arr)
        low = 0
        high = n-1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index
        
    def last(self, arr, target):
        n = len(arr)
        low = 0
        high = n-1
        index = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                index = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return index
    
    def countFreq(self, arr, target):
        f = self.first(arr, target)
        if f == -1:
            return 0
        l = self.last(arr, target)
        return (l-f)+1
    
        