def func(arr, n, result, idx, s, curr_sum):
    if idx == n:
        if curr_sum == s:
            return 1
        return 0
    include = func(arr, n, result, idx+1, s, curr_sum+arr[idx])
    exclude = func(arr, n, result, idx+1, s, curr_sum)
    return include + exclude

arr = list(map(int, input().split()))
n = len(arr)
result = []
print(func(arr, n, result, 0, 3, 0))
