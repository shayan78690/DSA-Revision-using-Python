class Solution(object):
    def cherryPickup(self, grid):
        n, m = len(grid), len(grid[0])
        return self.func(grid, n, m, 0, 0, m - 1)

    def func(self, grid, n, m, row, col1, col2):

        if col1 < 0 or col1 >= m or col2 < 0 or col2 >= m:
            return float('-inf')

        if row == n - 1:
            if col1 == col2:
                return grid[row][col1]
            return grid[row][col1] + grid[row][col2]

        if col1 == col2:
            current = grid[row][col1]
        else:
            current = grid[row][col1] + grid[row][col2]

        best = float('-inf')

        for move1 in [-1, 0, 1]:
            for move2 in [-1, 0, 1]:
                best = max(
                    best,
                    self.func(grid, n, m, row + 1, col1 + move1, col2 + move2)
                )

        return current + best


class Solution(object):
    def cherryPickup(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[[-1] * m for _ in range(m)] for _ in range(n)]
        return self.func(grid, n, m, 0, 0, m-1, dp)

    def func(self, grid, n, m, row, col1, col2, dp):
        if col1 < 0 or col1 >= m or col2 < 0 or col2 >= m:
            return float('-inf')
        
        if row == n-1:
            if col1 == col2:
                return grid[row][col1]
            return grid[row][col1] + grid[row][col2]
        
        if dp[row][col1][col2] != -1:
            return dp[row][col1][col2]
        
        if col1 == col2:
            current = grid[row][col1]
        else:
            current = grid[row][col1] + grid[row][col2]
        best = float('-inf')
        for move1 in [-1, 0, 1]:
            for move2 in [-1, 0, 1]:
                best = max(best, self.func(grid, n, m, row+1, col1+move1, col2+move2, dp))
        dp[row][col1][col2] = current + best
        return dp[row][col1][col2]


class Solution(object):
    def cherryPickup(self, grid):
        n, m = len(grid), len(grid[0])
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]
        for col1 in range(m):
            for col2 in range(m):
                if col1 == col2:
                    dp[n-1][col1][col2] = grid[n-1][col1]
                else:
                    dp[n-1][col1][col2] = grid[n-1][col1] + grid[n-1][col2]
        
        for row in range(n-2, -1, -1):
            for col1 in range(m):
                for col2 in range(m):
                    if col1 == col2:
                        current = grid[row][col1]
                    else:
                        current = grid[row][col1] + grid[row][col2]
                    best = float('-inf')
                    for move1 in [-1, 0, 1]:
                        for move2 in [-1, 0, 1]:
                            newCol1 = col1 + move1
                            newCol2 = col2 + move2
                            if 0 <= newCol1 < m and 0 <= newCol2 < m:
                                best = max(best, dp[row+1][newCol1][newCol2])
                    dp[row][col1][col2] = current + best
        return dp[0][0][m-1]


    
