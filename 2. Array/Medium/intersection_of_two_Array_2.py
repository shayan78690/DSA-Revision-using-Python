class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
        
        return ans
    
    
    
class Solution1:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = {}
        for i in nums1:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        temp = []
        for i in nums2:
            if i in m:
                temp.append(i)
                m[i] -= 1
                if m[i] == 0:
                    del m[i]
        ans = []
        for i in temp:
            ans.append(i)        
        return ans
        