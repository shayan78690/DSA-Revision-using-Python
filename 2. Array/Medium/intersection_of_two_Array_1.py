class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            if i in nums2 and i not in ans:
                ans.append(i)
        return ans
    
class Solution1:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = {}
        for i in nums1:
            s.add(i)
        ans = []
        for i in nums2:
            if i in s:
                ans.append(i)
                s.remove(i)
        return ans