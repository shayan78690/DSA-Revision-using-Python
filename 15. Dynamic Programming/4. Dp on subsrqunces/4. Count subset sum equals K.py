from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [[-1] * (k+1) for _ in range(n)]
    return func(arr, n, 0, k, dp)

def func(arr, n, index, k, dp):
    if k == 0:
        return 1
    if index == n:
        return 0
    if dp[index][k] != -1:
        return dp[index][k]
    exclude = func(arr, n, index+1, k, dp)
    include = 0
    if arr[index] <= k:
        include = func(arr, n, index+1, k-arr[index], dp)
    dp[index][k] = include + exclude
    return dp[index][k]
