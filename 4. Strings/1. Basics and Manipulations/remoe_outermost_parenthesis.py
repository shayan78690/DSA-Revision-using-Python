class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        lis = []
        for ch in s:
            if ch == '(':
                if count > 0:
                    lis.append(ch)
                count += 1
            else:
                count -= 1
                if count > 0:
                    lis.append(ch)
        return "".join(lis)