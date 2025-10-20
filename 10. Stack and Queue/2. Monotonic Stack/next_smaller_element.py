class Solution:
    @staticmethod
    def nextSmallerElement(arr):
        n = len(arr)
        result = []
        stack = []

        # Traverse from end to start
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            
            if not stack:
                result.append(-1)
            else:
                result.append(stack[-1])
            
            stack.append(arr[i])
        
        # Reverse result to match original order
        result.reverse()
        return result


# Example usage
if __name__ == "__main__":
    arr = [4, 5, 2, 10, 8]
    print(Solution.nextSmallerElement(arr))  # Output: [2, 2, -1, 8, -1]
