import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

class Solution(object):
    def isPalindrome(self, s):
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].lower() == s[right].lower():
                return False
            left += 1
            right -= 1
        return True

        
