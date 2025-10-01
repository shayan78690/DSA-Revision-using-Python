class Solution:
    
    def merge(self, nums, start, mid, end):
        left = start
        right = mid+1
        temp = []
        while left <= mid and right <= end:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1
        
        while left <= mid:
            temp.append(nums[left])
            left += 1
        
        while right <= end:
            temp.append(nums[right])
            right += 1
        
        for i in range(len(temp)):
            nums[start+i] = temp[i]
        
    def countPairs(self, nums, start, mid, end):
        count = 0
        j = mid+1
        for i in range(start, mid+1):
            while j <= end and nums[i] > 2 * nums[j]:
                j += 1
            count += (j-(mid+1))
        return count


    def mergeSort(self, nums, start, end):
        count = 0
        if start >= end:
            return count
        mid = (start + end) // 2
        count += self.mergeSort(nums, start, mid)
        count += self.mergeSort(nums, mid+1, end)
        count += self.countPairs(nums, start, mid, end)
        self.merge(nums, start, mid, end)
        return count

    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.mergeSort(nums, 0, len(nums)-1)