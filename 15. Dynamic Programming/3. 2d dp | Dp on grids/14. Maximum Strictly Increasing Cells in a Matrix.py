class Solution:
    def maxIncreasingCells(self, mat):
        m = len(mat)
        n = len(mat[0])

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, self.solve(mat, r, c))

        return ans

    def solve(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        ans = 1

        for nc in range(n):
            if mat[r][nc] > mat[r][c]:
                ans = max(
                    ans,
                    1 + self.solve(mat, r, nc)
                )

        for nr in range(m):
            if mat[nr][c] > mat[r][c]:
                ans = max(
                    ans,
                    1 + self.solve(mat, nr, c)
                )

        return ans




class Solution:
    def maxIncreasingCells(self, mat):
        m = len(mat)
        n = len(mat[0])

        dp = [[-1] * n for _ in range(m)]

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, self.solve(mat, r, c, dp))

        return ans

    def solve(self, mat, r, c, dp):
        if dp[r][c] != -1:
            return dp[r][c]

        m = len(mat)
        n = len(mat[0])

        ans = 1

        for nc in range(n):
            if mat[r][nc] > mat[r][c]:
                ans = max(
                    ans,
                    1 + self.solve(mat, r, nc, dp)
                )

        for nr in range(m):
            if mat[nr][c] > mat[r][c]:
                ans = max(
                    ans,
                    1 + self.solve(mat, nr, c, dp)
                )

        dp[r][c] = ans

        return ans
