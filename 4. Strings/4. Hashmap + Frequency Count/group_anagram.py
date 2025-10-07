class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            lis = list(s)
            lis.sort()
            string = "".join(lis)
            if string not in m:
                m[string] = []
            m[string].append(s)
        
        ans = []
        for key, value in m.items():
            ans.append(value)
        return ans
    
