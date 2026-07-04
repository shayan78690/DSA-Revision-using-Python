def reverse(arr, left, right):

    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    reverse(arr, left + 1, right - 1)
