class Solution:    
    def minPlatform(self, arr, dep):
        ans = 1
        n = len(arr)
        for i in range(n):
            count = 1
            for j in range(i+1, n):
                if (arr[i] >= arr[j] and arr[i] <= dep[j]) or \
                (arr[j] >= arr[i] and arr[j] <= dep[i]):
                    count += 1
            ans = max(ans, count)
        return ans




class Solution:
    def findPlatform(self, arr, dep):
        n = len(arr)
        arr.sort()
        dep.sort()

        i = 0
        j = 0
        count = 0
        maxCount = 0

        while i < n:
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1

            maxCount = max(maxCount, count)

        return maxCount
