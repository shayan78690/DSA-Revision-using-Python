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
