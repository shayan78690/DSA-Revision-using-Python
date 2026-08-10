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

        return False

   
