def func(arr, n, result, current, idx, s, curr_sum):
    if idx == n:
        if curr_sum == s:
            result.append(current[:])
            return True
        return False
    current.append(arr[idx])
    if func(arr, n, result, current, idx+1, s, curr_sum+arr[idx]):
        return True
    current.pop()
    if func(arr, n, result, current, idx+1, s, curr_sum):
        return True
    return False

arr = list(map(int, input().split()))
n = len(arr)
result = []
func(arr, n, result, [], 0, 3, 0)
print(result)
