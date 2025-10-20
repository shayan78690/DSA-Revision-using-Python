# Solution class to find next greater elements
class Solution:
    # Function to find next greater elements
    def nextGreater(self, nums):
        # Stack to store elements
        stack = []

        # Result array of same size
        n = len(nums)
        res = [0] * n

        # Traverse from right to left
        for i in range(n - 1, -1, -1):

            # Pop all smaller or equal elements
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            # If stack is empty, no greater element
            if not stack:
                res[i] = -1

            # Else top of stack is the answer
            else:
                res[i] = stack[-1]

            # Push current element
            stack.append(nums[i])

        # Return the result
        return res

# Main function
def main():
    nums = [4, 5, 2, 10]
    sol = Solution()
    ans = sol.nextGreater(nums)
    print(" ".join(map(str, ans)))

main()