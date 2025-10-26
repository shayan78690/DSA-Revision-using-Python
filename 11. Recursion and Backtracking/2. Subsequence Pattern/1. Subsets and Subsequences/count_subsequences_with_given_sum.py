class Solution(object):
    def perfectSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def findAllSubsequences(nums, idx, target, current_sum):
            if idx == len(nums):
                if current_sum == target:
                    return 1
                else:
                    return 0

            # Include nums[idx]
            current_sum += nums[idx]
            l = findAllSubsequences(nums, idx + 1, target, current_sum)

            # Exclude nums[idx]
            current_sum -= nums[idx]
            r = findAllSubsequences(nums, idx + 1, target, current_sum)

            return l + r

        return findAllSubsequences(nums, 0, target, 0)


# Example usage
if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target sum: "))
    solution = Solution()
    print(solution.perfectSum(nums, target))
