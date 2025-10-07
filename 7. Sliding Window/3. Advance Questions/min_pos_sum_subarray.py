def minimumSumSubarray(nums, l, r):
    minSum = float('inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            length = j - i + 1
            if l <= length <= r:
                if current_sum > 0:
                    minSum = min(current_sum, minSum)
    return -1 if minSum == float('inf') else minSum
