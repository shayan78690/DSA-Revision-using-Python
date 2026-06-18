class Solution:
    def nextLargerElement(self, arr):
        stack = []
        result = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            if not stack:
                result[i] = -1
            else:
                result[i] = stack[-1]
            stack.append(arr[i])
        return result
