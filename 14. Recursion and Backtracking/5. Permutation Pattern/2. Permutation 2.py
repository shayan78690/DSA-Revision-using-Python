class Solution(object):
    def permuteUnique(self, nums):
        n = len(nums)
        nums.sort()
        result = []
        visited = [False]*n
        self.func(nums, n, result, [], visited)
        return result
        
    def func(self, nums, n, result, current, visited):
        if len(current) == n:
            result.append(current[:])
            return
        for i in range(n):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: 
                continue
            current.append(nums[i])
            visited[i] = True
            self.func(nums, n, result, current, visited)
            visited[i] = False
            current.pop()
