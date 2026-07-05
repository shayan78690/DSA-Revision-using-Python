def func(arr, n, result, current, idx, s, curr_sum):
    if idx == n:
        if curr_sum == s:
            result.append(current[:])
        return
    current.append(arr[idx])
    include = func(arr, n, result, current, idx+1, s, curr_sum+arr[idx])
    current.pop()
    exclude = func(arr, n, result, current, idx+1, s, curr_sum)

arr = list(map(int, input().split()))
n = len(arr)
result = []
func(arr, n, result, [], 0, 3, 0)
print(result)
