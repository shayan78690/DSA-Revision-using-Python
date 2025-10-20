class Solution:
    def subArrayRanges(self, nums):
        n = len(nums)
        max_sum = self.sumOfSubarrayMaximum(nums, n)
        min_sum = self.sumOfSubarrayMinimum(nums, n)
        return max_sum - min_sum

    def sumOfSubarrayMinimum(self, nums, n):
        nse = self.findNSE(nums, n)
        pse = self.findPSE(nums, n)

        total = 0
        for i in range(n):
            first = nse[i] - i
            second = i - pse[i]
            total += nums[i] * first * second
        return total

    def sumOfSubarrayMaximum(self, nums, n):
        nle = self.findNLE(nums, n)
        ple = self.findPLE(nums, n)

        total = 0
        for i in range(n):
            first = nle[i] - i
            second = i - ple[i]
            total += nums[i] * first * second
        return total

    def findNSE(self, nums, n):
        nse = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse

    def findPSE(self, nums, n):
        pse = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse

    def findNLE(self, nums, n):
        nle = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            nle[i] = stack[-1] if stack else n
            stack.append(i)
        return nle

    def findPLE(self, nums, n):
        ple = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            ple[i] = stack[-1] if stack else -1
            stack.append(i)
        return ple


# Example usage
if __name__ == "__main__":
    obj = Solution()
    nums = [1, 2, 3]
    print(obj.subArrayRanges(nums))  # Output: 4
