class Solution(object):
    
    def isVowel(self, s):
        return s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u'

    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        left = 0
        right = 0
        count = 0
        max_count = 0
        while right < n:
            if self.isVowel(s[right]):
                count += 1
            while right-left+1 > k:
                if self.isVowel(s[left]):
                    count -= 1
                left += 1
            if right-left+1 == k:
                max_count = max(max_count, count)
            right += 1
        return max_count
