class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        heights = [[0] * m for _ in range(n)]
        
        for j in range(m):
            s = 0
            for i in range(n):
                if matrix[i][j] == '1':
                    s += 1
                else:
                    s = 0
                heights[i][j] = s
        
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, self.largestRectangleArea(heights[i]))
        return maxArea
        
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        nse = self.findNSE(heights, n)
        pse = self.findPSE(heights, n)
        maxi = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = width * heights[i]
            maxi = max(maxi, area)
        return maxi
    
    def findNSE(self, arr, n):
        nse = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse
    
    def findPSE(self, arr, n):
        pse = [0] * n
        stack = []
        for i in range(0, n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse
