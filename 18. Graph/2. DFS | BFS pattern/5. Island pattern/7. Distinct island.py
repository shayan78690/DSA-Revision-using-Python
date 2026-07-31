class Solution:
    def countDistinctIslands(self, grid):
        n, m = len(grid), len(grid[0])
        count = 0
        def dfs(r, c, dr, dc, shape):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == "W":
                return 0
            grid[r][c] = "W"
            shape.append((r-dr, c-dc))
            dfs(r+1, c, dr, dc, shape)
            dfs(r-1, c, dr, dc, shape)
            dfs(r, c+1, dr, dc, shape)
            dfs(r, c-1, dr, dc, shape)

        hashset = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "L":
                    shape = []
                    dfs(i, j, i, j, shape)
                    hashset.add(tuple(shape))
        return len(hashset)
