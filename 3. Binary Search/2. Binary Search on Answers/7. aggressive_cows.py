def tempFunc(stalls, k, dist):
    last = stalls[0]
    cows = 1
    for i in range(1, len(stalls)):
        if stalls[i] - last >= dist:
            cows += 1
            last = stalls[i]
            
        if cows >= k:
            return True
    return False

def func(stalls, k):
    stalls.sort()
    n = len(stalls)
    low = 1
    high = stalls[n-1] - stalls[0]
    result = low 
    while low <= high:
        mid = (low + high) // 2
        if tempFunc(stalls, k, mid):
            result = mid
            low = mid+1
        else:
            high = mid-1
    return result

stalls = list(map(int, input().split(",")))
k = int(input())
result = func(stalls, k)
print(result)
