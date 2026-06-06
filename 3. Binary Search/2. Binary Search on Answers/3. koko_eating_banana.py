import math

def func2(piles, hours):
    total = 0
    for pile in piles:
        total += math.ceil(pile / hours)
    return total

def func1(piles, h):
    low = 1
    high = max(piles)
    result = high
    while low <= high:
        mid = (low + high) // 2
        hours = func2(piles, mid)
        if hours <= h:
            result = mid
            high = mid-1
        else:
            low = mid+1
    return result

piles = list(map(int, input().split(",")))
h = int(input())
result = func1(piles, h)
print(result)
