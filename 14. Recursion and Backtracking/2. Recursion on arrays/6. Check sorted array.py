def isSorted(arr, i):

    if i == len(arr)-1:
        return True

    if arr[i] > arr[i+1]:
        return False

    return isSorted(arr, i + 1)
