class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        ans = nums1 + nums2
        ans.sort()
        n = len(ans)
        if n % 2 == 1:
            return ans[n//2]
        else:
            return (ans[n//2 - 1] + ans[n//2]) / 2.0 



class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        n = n1 + n2
        low = 0
        high = n1
        left = (n1 + n2 + 1) // 2
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = nums1[mid1-1] if mid1 > 0 else float('-inf')
            l2 = nums2[mid2-1] if mid2 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < n1 else float('inf')
            r2 = nums2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1-1
            else:
                low = mid1+1
        return 0