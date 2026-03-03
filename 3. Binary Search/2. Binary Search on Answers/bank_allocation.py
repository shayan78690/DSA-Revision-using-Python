import math

def tempFunc(arr, m, pages):
    student = 1
    total = 0
    for i in range(len(arr)):
        if arr[i] + total <= pages:
            total += arr[i]
        else:
            student += 1
            total = arr[i]
    return student

def func(arr, m):
    n = len(arr)
    if n < m:
        return -1
    low = max(arr)
    high = sum(arr)
    result = high
    while low <= high:
        mid = (low + high) // 2
        ans = tempFunc(arr, m, mid)
        if ans <= m:
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result

arr = list(map(int, input().split(",")))
m = int(input())
result = func(arr, m)
print(result)
