class Solution(object):
    def subsetsWithDup(self, nums):
        n = len(nums)
        nums.sort()
        result = []
        self.func(nums, n, result, [], 0)
        return result

    def func(self, nums, n, result, current, idx):
        if idx == n:
            result.append(current[:])
            return
        current.append(nums[idx])
        self.func(nums, n, result, current, idx+1)
        current.pop()
        while idx+1 < n and nums[idx] == nums[idx+1]:
            idx += 1
        self.func(nums, n, result, current, idx+1)



def func(arr, start, current, result):
    result.append(current[:])

    for i in range(start, len(arr)):

        if i > start and arr[i] == arr[i-1]:
            continue

        current.append(arr[i])

        func(arr, i+1, current, result)

        current.pop()


arr = list(map(int, input().split()))
arr.sort()

result = []
func(arr, 0, [], result)

print(result)
