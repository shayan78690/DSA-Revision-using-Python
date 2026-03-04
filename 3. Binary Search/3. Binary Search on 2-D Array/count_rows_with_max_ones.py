def lowerBound(arr, n, x):
    low = 0
    high = n-1
    result = high
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result

def func(arr, n, m):
    max_count = 0
    index = -1
    for i in range(n):
        ones = m - lowerBound(arr[i], m, 1)
        if ones > max_count:
            max_count = ones
            index = i
    return index

n, m = map(int, input().split())
arr = [list(map(int, input().split(","))) for _ in range(n)]
result = func(arr, n, m)
print(result)
