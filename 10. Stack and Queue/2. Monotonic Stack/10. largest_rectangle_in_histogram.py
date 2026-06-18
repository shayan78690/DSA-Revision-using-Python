class Solution:
    def largestRectangleArea(self, arr):
        n = len(arr)
        maxArea = 0
        pse = self.findPSE(arr, n)
        nse = self.findNSE(arr, n)

        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = arr[i] * width
            maxArea = max(area, maxArea)
        
        return maxArea

    def findNSE(self, arr, n):
        nse = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse

    def findPSE(self, arr, n):
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
    obj = Solution()
    heights = [2,1,5,6,2,3]
    print(obj.largestRectangleArea(heights))  # Output: 10
