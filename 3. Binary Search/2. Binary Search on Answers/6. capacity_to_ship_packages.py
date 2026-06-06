import math

def func2(weights, days, capacity):
    day = 1
    total = 0
    for i in range(len(weights)):
        if total + weights[i] > capacity:
            day += 1
            total = weights[i]
        else:
            total += weights[i]
    return day <= days

def func1(weights, days):
    low = max(weights)
    high = sum(weights)
    result = high
    while low <= high:
        mid = (low + high) // 2
        if func2(weights, days, mid):
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result


weights = list(map(int, input().split(",")))
days = int(input())
result = func1(weights, days)
print(result)
