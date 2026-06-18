class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        stack = []
        result = [0] * n
        for i in range(n-1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0
            stack.append(i)
        return result
        
