def maximum(arr, i):

    if i == len(arr)-1:
        return arr[i]

    return max(arr[i], maximum(arr, i + 1))
