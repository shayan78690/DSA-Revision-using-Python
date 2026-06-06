class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)


class Solution(object):
    def minAddToMakeValid(self, s):
        opening = 0
        insertion = 0
        for ch in s:
            if ch == '(':
                opening += 1
            else:
                if opening > 0:
                    opening -= 1
                else:
                    insertion += 1
        return opening + insertion
        
        
