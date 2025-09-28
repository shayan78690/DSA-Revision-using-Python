class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        dup = x
        while dup != 0:
            ld =  dup % 10
            rev = rev * 10 + ld
            dup = dup // 10
        if rev == x:
            return True
        else:
            return False
        