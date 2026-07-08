def frogJump(heights, n, k):
    return func(heights, n, 0, k)

def func(heights, n, index, k):
    if index == n-1:
        return 0
    ans = float('inf')
    for jump in range(1, k+1):
        if index+jump < n:
            cost = abs(heights[index]-heights[index+jump])
            ans = min(ans, cost+func(heights, n, index+jump, k))
    return ans
            

heights = list(map(int, input().split(",")))
k = int(input())
n = len(heights)
print(frogJump(heights, n, k))





def frogJump(heights, n, k):
    dp = [-1] * n
    return func(heights, n, 0, k, dp)

def func(heights, n, index, k, dp):
    if index == n - 1:
        return 0

    if dp[index] != -1:
        return dp[index]

    ans = float('inf')

    for jump in range(1, k + 1):
        if index + jump < n:
            cost = abs(heights[index] - heights[index + jump])
            ans = min(ans, cost + func(heights, n, index + jump, k, dp))

    dp[index] = ans
    return dp[index]

heights = list(map(int, input().split(",")))
k = int(input())
n = len(heights)
print(frogJump(heights, n, k))








def frogJump(heights, n, k):
    dp = [0] * n
    dp[n-1] = 0
    for i in range(n-2, -1, -1):
        ans = float('inf')
        for jump in range(1, k+1):
            if i + jump < n:
                cost = abs(heights[i]-heights[i+jump])
                ans = min(ans, cost+dp[i+jump])
        dp[i] = ans
    return dp[0]


            

heights = list(map(int, input().split(",")))
k = int(input())
n = len(heights)
print(frogJump(heights, n, k))
            


