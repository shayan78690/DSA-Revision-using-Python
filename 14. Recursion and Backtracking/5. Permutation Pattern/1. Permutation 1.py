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



class Solution(object):
    def permute(self, nums):
        result = []
        self.func(nums, 0, result)
        return result

    def func(self, nums, index, result):
        if index == len(nums):
            result.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]

            self.func(nums, index + 1, result)

            nums[index], nums[i] = nums[i], nums[index]
