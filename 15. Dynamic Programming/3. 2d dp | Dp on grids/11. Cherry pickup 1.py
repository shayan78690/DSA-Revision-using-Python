class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)
        dp = [[[-1]*n for _ in range(n)] for _ in range(n)]
        return max(0, self.solve(grid, 0, 0, 0, n,dp))

    def solve(self, grid, r1, c1, r2, n, dp):

        c2 = r1 + c1 - r2

        if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
            return float('-inf')

        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float('-inf')

        if r1 == n - 1 and c1 == n - 1:
            return grid[r1][c1]
        if dp[r1][c1][r2] != -1:
            return dp[r1][c1][r2]

        if r1 == r2 and c1 == c2:
            current = grid[r1][c1]
        else:
            current = grid[r1][c1] + grid[r2][c2]

        down_down = self.solve(grid, r1 + 1, c1, r2 + 1, n, dp)

        down_right = self.solve(grid, r1 + 1, c1, r2, n, dp)

        right_down = self.solve(grid, r1, c1 + 1, r2 + 1, n, dp)

        right_right = self.solve(grid, r1, c1 + 1, r2, n, dp)

        dp[r1][c1][r2] = current + max(
            down_down,
            down_right,
            right_down,
            right_right
        )
        return dp[r1][c1][r2]




class Solution(object):
    def cherryPickup(self, grid):
        n = len(grid)

        dp = [[[float('-inf')] * n for _ in range(n)] for _ in range(n)]

        dp[n - 1][n - 1][n - 1] = grid[n - 1][n - 1]

        for r1 in range(n - 1, -1, -1):
            for c1 in range(n - 1, -1, -1):
                for r2 in range(n - 1, -1, -1):

                    if r1 == n - 1 and c1 == n - 1:
                        continue

                    c2 = r1 + c1 - r2

                    if c2 < 0 or c2 >= n:
                        continue

                    if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                        continue

                    if r1 == r2 and c1 == c2:
                        current = grid[r1][c1]
                    else:
                        current = grid[r1][c1] + grid[r2][c2]

                    down_down = float('-inf')
                    if r1 + 1 < n and r2 + 1 < n:
                        down_down = dp[r1 + 1][c1][r2 + 1]

                    down_right = float('-inf')
                    if r1 + 1 < n:
                        down_right = dp[r1 + 1][c1][r2]

                    right_down = float('-inf')
                    if c1 + 1 < n and r2 + 1 < n:
                        right_down = dp[r1][c1 + 1][r2 + 1]

                    right_right = float('-inf')
                    if c1 + 1 < n:
                        right_right = dp[r1][c1 + 1][r2]

                    dp[r1][c1][r2] = current + max(
                        down_down,
                        down_right,
                        right_down,
                        right_right
                    )

        return max(0, dp[0][0][0])
