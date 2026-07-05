class Solution(object):
    def permute(self, nums):
        n = len(nums)
        result = []
        visited = [False] * n
        self.func(nums, n, result, [], visited)
        return result
    
    def func(self, nums, n, result, current, visited):
        if len(current) == n:
            result.append(current[:])
            return   
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            current.append(nums[i])
            self.func(nums, n, result, current, visited)
            visited[i] = False
            current.pop()      

