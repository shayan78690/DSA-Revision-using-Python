class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        stack = []
        res = [0] * n

        for i in range(2*n - 1, -1, -1):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if not stack:
                    res[i % n] = -1
                else:
                    res[i % n] = stack[-1]

            stack.append(nums[i % n])

        return res


# Example usage
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 1]
    print(obj.nextGreaterElements(nums))  # Output: [2, -1, 2]
