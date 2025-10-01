class Solution:
    
    def merge(self, arr, start, mid, end):
        left = start
        right = mid+1
        temp = []
        count = 0
        while left <= mid and right <= end:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                count += (mid-left+1)
                right += 1
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= end:
            temp.append(arr[right])
            right += 1
            
        for i in range(len(temp)):
            arr[start + i] = temp[i]

        return count
        
    
    def mergeSort(self, arr, start, end):
        count = 0
        if start >= end:
            return count
        mid = (start + end) // 2
        count += self.mergeSort(arr, start, mid)
        count += self.mergeSort(arr, mid+1, end)
        count += self.merge(arr, start, mid, end)
        return count
    
    def inversionCount(self, arr):
        return self.mergeSort(arr, 0, len(arr)-1)
    
    