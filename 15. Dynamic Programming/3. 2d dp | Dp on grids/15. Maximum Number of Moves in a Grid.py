class Solution:
    def maxMoves(self, grid):
        m = len(grid)
        n = len(grid[0])

        ans = 0

        for r in range(m):
            ans = max(ans, self.solve(grid, r, 0))

        return ans

    def solve(self, grid, r, c):
        m = len(grid)
        n = len(grid[0])
        if c == n - 1:
            return 0
        ans = 0
        directions = [
            (-1, 1),
            (0, 1),
            (1, 1)
        ]
        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] > grid[r][c]:
                    ans = max(
                        ans,
                        1 + self.solve(grid, nr, nc)
                    )




class Solution:
    def maxMoves(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        ans = 0

        for r in range(m):
            ans = max(ans, self.solve(grid, r, 0, dp))
        return ans

    def solve(self, grid, r, c, dp):
        if dp[r][c] != -1:
            return dp[r][c]
        m = len(grid)
        n = len(grid[0])
        if c == n - 1:
            return 0
        ans = 0
        directions = [-1, 0, 1]

        for dr in directions:
            nr = r + dr
            nc = c + 1
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] > grid[r][c]:
                    ans = max(ans, 1 + self.solve(grid, nr, nc, dp))
        dp[r][c] = ans
        return ans
        return ans
