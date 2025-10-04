class Solution:
    
    def func(self, arr, k, pages):
        count_Students = 1
        pagesCount = 0
        for i in range(len(arr)):
            if pagesCount + arr[i] <= pages:
                pagesCount += arr[i]
            else:
                count_Students += 1
                pagesCount = arr[i]
        return count_Students
    
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:
            return -1
        low = max(arr)
        high = sum(arr)
        ans = -1
        while low <= high:
            mid = (low+high)//2
            temp = self.func(arr, k, mid)
            if temp <= k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
