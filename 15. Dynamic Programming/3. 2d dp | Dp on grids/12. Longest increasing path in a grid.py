class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, self.solve(matrix, r, c))

        return ans

    def solve(self, matrix, r, c):
        m = len(matrix)
        n = len(matrix[0])

        ans = 1

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
                if matrix[nr][nc] > matrix[r][c]:
                    ans = max(
                        ans,
                        1 + self.solve(matrix, nr, nc)
                    )

        return ans


class Solution:
    def longestIncreasingPath(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        dp = [[-1] * n for _ in range(m)]

        ans = 0

        for r in range(m):
            for c in range(n):
                ans = max(ans, self.solve(matrix, r, c, dp))

        return ans

    def solve(self, matrix, r, c, dp):
        if dp[r][c] != -1:
            return dp[r][c]

        m = len(matrix)
        n = len(matrix[0])

        ans = 1

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
                if matrix[nr][nc] > matrix[r][c]:
                    ans = max(
                        ans,
                        1 + self.solve(matrix, nr, nc, dp)
                    )

        dp[r][c] = ans

        return ans



