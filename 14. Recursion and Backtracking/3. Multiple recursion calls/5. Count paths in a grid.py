def ways(curr, target):

    if curr == target:
        return 1

    if curr > target:
        return 0

    return ways(curr+1, target) + ways(curr+2, target)
