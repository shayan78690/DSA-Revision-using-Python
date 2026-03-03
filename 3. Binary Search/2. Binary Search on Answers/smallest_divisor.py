import math

def func2(arr, limit, divisor):
    total = 0
    for i in range(len(arr)):
        total += math.ceil(arr[i] / divisor)
    return total

def func1(arr, limit):
    low = 1
    high = max(arr)
    result = high
    while low <= high:
        mid = (low + high) // 2
        ans = func2(arr, limit, mid)
        if ans <= limit:
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result
    
    


arr = list(map(int, input().split(",")))
limit = int(input())
result = func1(arr, limit)
print(result)
