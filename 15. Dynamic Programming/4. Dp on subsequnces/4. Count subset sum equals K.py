from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    mod = 10**9+7
    dp = [[-1] * (k+1) for _ in range(n)]
    return func(arr, n, 0, k, dp) % mod

def func(arr, n, index, k, dp):
    if index == n:
        return 1 if k == 0 else 0

    if dp[index][k] != -1:
        return dp[index][k]

    exclude = func(arr, n, index + 1, k, dp)

    include = 0
    if arr[index] <= k:
        include = func(arr, n, index + 1, k - arr[index], dp)

    dp[index][k] = include + exclude
    return dp[index][k]


from typing import List

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    mod = 10**9+7
    dp = [[0] * (k+1) for _ in range(n+1)]
    dp[n][0] = 1
    for index in range(n-1, -1, -1):
        for target in range(k+1):
            exclude = dp[index+1][target]
            include = 0
            if arr[index] <= target:
                include = dp[index+1][target-arr[index]]
            dp[index][target] = include + exclude
    return dp[0][target] % mod

