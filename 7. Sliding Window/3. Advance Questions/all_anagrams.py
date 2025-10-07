class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        left = 0
        right = 0
        ans = []
        while right < n:
            if right-left+1 > m:
                left += 1
            if right-left+1 == m:
                if self.isAnagram(s[left:right+1], p):
                    ans.append(left)
            right += 1
        return ans
    def isAnagram(self, s, p):
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(p[i]) - ord('a')] -= 1
        
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True