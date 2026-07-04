def solve(arr, i):

    if i == len(arr):
        return

    # Process current element
    process(arr[i])

    solve(arr, i + 1)
