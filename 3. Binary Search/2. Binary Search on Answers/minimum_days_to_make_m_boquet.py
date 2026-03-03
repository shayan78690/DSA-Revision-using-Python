import math

def func2(arr, m, k, day):
    flowers = 0
    boquet = 0
    for i in range(len(arr)):
        if arr[i] <= day:
            flowers += 1
            if flowers == k:
                boquet += 1
                flowers = 0
        else:
            flowers = 0
    return boquet >= m

def func1(arr, m, k):
    if len(arr) < m*k:
        return -1
    low = min(arr)
    high = max(arr)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if func2(arr, m, k, mid):
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result
    


arr = list(map(int, input().split(",")))
m, k = map(int, input().split(","))
result = func1(arr, m, k)
print(result)
