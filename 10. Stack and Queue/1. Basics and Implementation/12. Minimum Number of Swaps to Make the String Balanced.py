class Solution(object):
    def minSwaps(self, s):
        stack = []
        for ch in s:
            if ch == '[':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
        return (len(stack)+1)//2
        
