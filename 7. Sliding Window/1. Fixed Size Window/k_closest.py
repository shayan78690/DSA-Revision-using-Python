class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left = 0
        right = len(arr)-1
        while right-left+1 > k:
            if abs(arr[left]-x) > abs(arr[right]-x):
                left += 1
            else:
                right -= 1
        
        ans = []
        for i in range(left, right+1):
            ans.append(arr[i])
        return ans
        