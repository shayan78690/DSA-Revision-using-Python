class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if stack:
                    if ((ch == ')' and stack[-1] == '(') or  (ch == ']' and stack[-1] == '[')
                    or  (ch == '}' and stack[-1] == '{')):
                        stack.pop()
                        continue
                    else:
                        return False
                else:
                    return False
            
        return len(stack) == 0
