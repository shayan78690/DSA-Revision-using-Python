def search(arr, i, target):

    if i == len(arr):
        return False

    if arr[i] == target:
        return True

    return search(arr, i + 1, target)
