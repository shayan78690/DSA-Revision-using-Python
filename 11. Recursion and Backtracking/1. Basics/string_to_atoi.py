class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        sign = 1
        i = 0
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if res > (2**31 - 1 - digit) // 10:
                return 2**31-1 if sign == 1 else -2**31
            res = res * 10 + digit
            i += 1
        return res * sign