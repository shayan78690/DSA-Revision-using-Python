class Solution(object):
    def longestIncreasingPath(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        ans = 0

        for r in range(n):
            for c in range(m):
                ans = max(ans, self.solve(matrix, r, c, 0, n, m))

        return ans

    def solve(self, matrix, r, c, teleport, n, m):

        best = 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if matrix[nr][nc] > matrix[r][c]:

                best = max(
                    best,
                    1 + self.solve(
                        matrix, nr, nc, teleport, n, m
                    )
                )

        if teleport == 0:

            for nr in range(n):
                for nc in range(m):

                    if matrix[nr][nc] > matrix[r][c]:

                        best = max(
                            best,
                            1 + self.solve(
                                matrix, nr, nc, 1, n, m
                            )
                        )

        return best


class Solution(object):
    def longestIncreasingPath(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        dp = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

        ans = 0

        for r in range(n):
            for c in range(m):
                ans = max(
                    ans,
                    self.solve(matrix, r, c, 0, n, m, dp)
                )

        return ans

    def solve(self, matrix, r, c, teleport, n, m, dp):

        if dp[r][c][teleport] != -1:
            return dp[r][c][teleport]

        best = 1

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            nr = r + dr
            nc = c + dc

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue

            if matrix[nr][nc] > matrix[r][c]:

                best = max(
                    best,
                    1 + self.solve(
                        matrix,
                        nr,
                        nc,
                        teleport,
                        n,
                        m,
                        dp
                    )
                )

        if teleport == 0:

            for nr in range(n):
                for nc in range(m):

                    if matrix[nr][nc] > matrix[r][c]:

                        best = max(
                            best,
                            1 + self.solve(
                                matrix,
                                nr,
                                nc,
                                1,
                                n,
                                m,
                                dp
                            )
                        )

        dp[r][c][teleport] = best

        return best
