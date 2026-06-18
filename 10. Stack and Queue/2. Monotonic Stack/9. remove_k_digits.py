class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for x in num:
            while stack and k > 0 and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)
        while stack and k > 0:
            stack.pop()
            k -= 1
        
        res = "".join(stack)
        res = res.lstrip("0")
        return res if res else "0"
