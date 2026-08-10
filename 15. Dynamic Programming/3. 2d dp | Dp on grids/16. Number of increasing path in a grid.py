class Solution:
    def countPaths(self, grid):
        m = len(grid)
        n = len(grid[0])

        MOD = 10**9 + 7

        dp = [[-1] * n for _ in range(m)]

        ans = 0

        for r in range(m):
            for c in range(n):
                ans += self.solve(grid, r, c, dp)
                ans %= MOD

        return ans

    def solve(self, grid, r, c, dp):
        if dp[r][c] != -1:
            return dp[r][c]

        m = len(grid)
        n = len(grid[0])

        MOD = 10**9 + 7

        count = 1

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] > grid[r][c]:
                    count += self.solve(grid, nr, nc, dp)
                    count %= MOD

        dp[r][c] = count

        return count
