class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n > m:
            return False
        count = [0] * 26
        for i in range(n):
            count[ord(s1[i]) - ord('a')] += 1
            count[ord(s2[i]) - ord('a')] -= 1
        
        if self.allZeroes(count):
            return True
        
        for i in range(n, m):
            count[ord(s2[i]) - ord('a')] -= 1
            count[ord(s2[i - n]) - ord('a')] += 1

            if self.allZeroes(count):
                return True
        return False

    def allZeroes(self, count):
        for i in range(len(count)):
            if count[i] != 0:
                return False
        return True