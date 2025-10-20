class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        n = len(num)

        for i in range(n):
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        # Remove remaining digits if k > 0
        while stack and k > 0:
            stack.pop()
            k -= 1

        # Build the result
        res = ''.join(stack)

        # Remove leading zeros
        res = res.lstrip('0')

        # Return result or "0" if empty
        return res if res else "0"
