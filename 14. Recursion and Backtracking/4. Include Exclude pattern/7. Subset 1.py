def func(arr, n, result, current, idx):
    if idx == n:
        result.append(current[:])
        return
    current.append(arr[idx])
    func(arr, n, result, current, idx+1)
    current.pop()
    func(arr, n, result, current, idx+1)

arr = list(map(int, input().split()))
n = len(arr)
result = []
func(arr, n, result, [], 0)
print(result)
