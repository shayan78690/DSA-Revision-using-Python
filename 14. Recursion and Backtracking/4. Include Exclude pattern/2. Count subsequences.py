def func(arr, n, result, current, idx):
    if idx == n:
        return 1
    current.append(arr[idx])
    include = func(arr, n, result, current, idx+1)
    current.pop()
    exclude = func(arr, n, result, current, idx+1)
    return include + exclude

arr = list(map(int, input().split()))
n = len(arr)
result = []
print(func(arr, n, result, [], 0))
