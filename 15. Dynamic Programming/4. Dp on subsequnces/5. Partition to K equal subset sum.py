class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        n = len(nums)
        
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        visited = [False] * n
        return self.func(nums, n, target, 0, 0, visited, k)
    
    def func(self, nums, n, target, start, curr, visited, k):
        if k == 1:
            return True
        if curr == target:
            return self.func(nums, n, target, 0, 0, visited, k-1)
        for i in range(start, n):
            if visited[i]:
                continue
            if nums[i] + curr > target:
                continue
            visited[i] = True
            if self.func(nums, n, target, i+1, curr+nums[i], visited, k):
                return True
            visited[i] = False




class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        used = [False] * len(nums)
        return self.solve(nums, used, k, 0, 0, target)

    def solve(self, nums, used, k, start, currSum, target):
        if k == 1:
            return True
        if currSum == target:
            return self.solve(nums, used, k - 1, 0, 0, target)
        prev = -1
        for i in range(start, len(nums)):
            if used[i]:
                continue
            if nums[i] == prev:
                continue

            if currSum + nums[i] > target:
                continue

            used[i] = True

            if self.solve(nums, used, k, i + 1, currSum + nums[i], target):
                return True

            used[i] = False

            prev = nums[i]

            if currSum == 0:
                break

        return False
        return False

   
