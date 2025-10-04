class Solution:
    
    def func(self, arr, m, x):
        low = 0
        ans = m
        high = len(arr)-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
            
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        max_count = 0
        index = -1
        for i in range(n):
            ones = m - self.func(arr[i], m, 1)
            if ones > max_count:
                max_count = ones
                index = i
        return index