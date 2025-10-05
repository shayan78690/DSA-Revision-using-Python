class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 in map1 and map1[c1] != c2) or (c2 in map2 and map2[c2] != c1):
                return False
            else:
                map1[c1] = c2
                map2[c2] = c1
        return True