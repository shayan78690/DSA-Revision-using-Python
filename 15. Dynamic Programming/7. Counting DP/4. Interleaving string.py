class Solution(object):
    def isInterleave(self, s1, s2, s3):
        n, m = len(s1), len(s2)
        if (n+m) != len(s3):
            return False
        dp = [[None] * (m+1) for _ in range(n+1)]
        def solve(i, j):
            if i == n and j == m:
                return True
            if dp[i][j] is not None:
                return dp[i][j]
            k = i+j
            if (i < n and s1[i] == s3[k] and j < m and s2[j] == s3[k]):
                dp[i][j] = solve(i+1, j) or solve(i, j+1)
            elif i < n and s1[i] == s3[k]:
                dp[i][j] = solve(i+1, j)
            elif j < m and s2[j] == s3[k]:
                dp[i][j] = solve(i, j+1)
            else:
                dp[i][j] = False
            return dp[i][j]
        return solve(0, 0)

        
