def countOccurrence(arr, i, target):

    if i == len(arr):
        return 0

    if arr[i] == target:
        return 1 + countOccurrence(arr, i + 1, target)

    return countOccurrence(arr, i + 1, target)
