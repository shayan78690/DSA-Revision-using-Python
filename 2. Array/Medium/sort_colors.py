class Solution(object):
    
    def merge(self, nums, low, mid, high):
        i = low
        j = mid+1
        temp = []
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= high:
            temp.append(nums[j])
            j += 1
        
        for i in range(len(temp)):
            nums[i+low] = temp[i]
        

    def mergeSort(self, nums, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid+1, end)
        self.merge(nums, start, mid, end)

    def sortColors(self, nums):
        self.mergeSort(nums, 0, len(nums)-1)
    
        
        
class Solution1(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                mid += 1
                low += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                
            
            