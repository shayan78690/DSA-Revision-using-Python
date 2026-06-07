class Solution(object):
    def reverseParentheses(self, s):
        stack = []
        for ch in s:
            if ch == ')':
                temp = []
                while stack and stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()
                for x in temp:
                    stack.append(x)
            else:
                stack.append(ch)
        
        return "".join(stack)
