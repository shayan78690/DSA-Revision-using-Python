class Solution:
    def sumSubarrayMins(self, arr):
        n = len(arr)
        nse = self.findNSE(arr, n)
        pse = self.findPSE(arr, n)
        mod = 10**9 + 7

        total = 0
        for i in range(n):
            first = nse[i] - i
            second = i - pse[i]
            total = (total + arr[i] * first * second) % mod
        
        return total

    def findNSE(self, arr, n):
        nse = [0] * n
        stack = []
        # Next Smaller Element to the right
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse

    def findPSE(self, arr, n):
        pse = [0] * n
        stack = []
        # Previous Smaller Element to the left
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse


# Example usage
if __name__ == "__main__":
    obj = Solution()
    arr = [3, 1, 2, 4]
    print(obj.sumSubarrayMins(arr))  # Output: 17
