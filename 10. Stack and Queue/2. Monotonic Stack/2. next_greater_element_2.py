class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [0] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            while stack and stack[-1] <= nums[i%n]:
                stack.pop()
            if stack:
                result[i%n] = stack[-1]
            else:
                result[i%n] = -1
            stack.append(nums[i%n])
        return result
