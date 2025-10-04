def func(boards, k, mid):
    count = 1
    s = 0
    for i in range(len(boards)):
        if s + boards[i] <= mid:
            s += boards[i]
        else:
            count += 1
            s = boards[i]
    return count

def findLargestMinDistance(boards:list, k:int):
    n = len(boards)
    if n < k:
        return -1
    low = max(boards)
    high = sum(boards)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        temp = func(boards, k, mid)
        if temp <= k:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans