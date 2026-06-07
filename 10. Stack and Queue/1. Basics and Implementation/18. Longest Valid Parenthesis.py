class Solution(object):
    def longestValidParentheses(self, s):
        n = len(s)
        stack = [-1]
        maxi = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                maxi = max(maxi, i-stack[-1])
        return maxi
        
