class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                else:
                    if (ch == ')' and stack[-1] == '(') or (ch == '}' and stack[-1] == '{') or (ch == ']' and stack[-1] == '['):
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
        
