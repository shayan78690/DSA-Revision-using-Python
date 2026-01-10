class Solution1:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(0, n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
obj = Solution()
arr = [5, 4, 3, 2, 1]
print(obj.bubbleSort(arr))

class Solution2:
    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(0, n):
          swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            if not swapped:
              break
        return arr
    
obj = Solution()
arr = [5, 4, 3, 2, 1]
print(obj.bubbleSort(arr))
