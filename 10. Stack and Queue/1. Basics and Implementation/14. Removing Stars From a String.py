class Solution(object):
    def removeStars(self, s):
        stack = []
        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                stack.pop()
        return "".join(stack)
        
