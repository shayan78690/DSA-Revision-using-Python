def firstOccurrence(arr, i, target):

    if i == len(arr):
        return -1

    if arr[i] == target:
        return i

    return firstOccurrence(arr, i + 1, target)


def lastOccurrence(arr, i, target):

    if i == len(arr):
        return -1

    ans = lastOccurrence(arr, i + 1, target)

    if ans != -1:
        return ans

    if arr[i] == target:
        return i

    return -1
