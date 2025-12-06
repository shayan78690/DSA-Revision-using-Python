class Solution:
    @staticmethod
    def maximalRectangle(matrix):
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        m = len(matrix[0])
        maxArea = 0
        heights = [[0] * m for _ in range(n)]

        # Build heights matrix
        for j in range(m):
            sum_ = 0
            for i in range(n):
                if matrix[i][j] == '1':
                    sum_ += 1
                else:
                    sum_ = 0
                heights[i][j] = sum_

        # Compute max rectangle for each row as histogram
        for i in range(n):
            maxArea = max(maxArea, Solution.largestRectangleHistogram(heights[i]))
        
        return maxArea

    @staticmethod
    def largestRectangleHistogram(arr):
        n = len(arr)
        nse = Solution.findNSE(arr, n)
        pse = Solution.findPSE(arr, n)

        maxArea = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = arr[i] * width
            maxArea = max(maxArea, area)
        return maxArea

    @staticmethod
    def findNSE(arr, n):
        nse = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse

    @staticmethod
    def findPSE(arr, n):
        pse = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse


# Example usage
if __name__ == "__main__":
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    print(Solution.maximalRectangle(matrix))  # Output: 6
