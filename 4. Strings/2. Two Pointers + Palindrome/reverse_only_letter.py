class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        n = len(arr)
        i = 0
        j = n-1
        while i < j:
            if not arr[i].isalpha():
                i += 1
            elif not arr[j].isalpha():
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return "".join(arr)
                
        