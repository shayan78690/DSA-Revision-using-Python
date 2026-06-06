class Solution:
    def duplicateParenthesis(self, s):

        stack = []

        for ch in s:

            if ch == ')':

                count = 0

                while stack and stack[-1] != '(':
                    stack.pop()
                    count += 1

                stack.pop()   # remove '('

                if count <= 1:
                    return True

            else:
                stack.append(ch)

        return False
