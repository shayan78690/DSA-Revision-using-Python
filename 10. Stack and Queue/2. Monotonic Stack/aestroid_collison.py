class Solution:
    def asteroidCollision(self, arr):
        n = len(arr)
        stack = []

        for i in range(n):
            if arr[i] > 0:
                stack.append(arr[i])
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(arr[i]):
                    stack.pop()
                if stack and stack[-1] == abs(arr[i]):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(arr[i])

        return stack


# Example usage
if __name__ == "__main__":
    obj = Solution()
    asteroids = [5, 10, -5]
    print(obj.asteroidCollision(asteroids))  # Output: [5, 10]

    asteroids = [8, -8]
    print(obj.asteroidCollision(asteroids))  # Output: []
