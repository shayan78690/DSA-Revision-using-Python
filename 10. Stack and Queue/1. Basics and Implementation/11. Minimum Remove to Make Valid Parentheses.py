class Solution(object):
    def minRemoveToMakeValid(self, s):
        left = 0
        right = 0
        stack = []
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                right += 1
            
            if right > left:
                right -= 1
                continue
            else:
                stack.append(ch)
        result = []
        while stack:
            ch = stack.pop()
            if left > right and ch == '(':
                left -= 1
            else:
                result.append(ch)
        result = reversed(result)
        return "".join(result)
        
