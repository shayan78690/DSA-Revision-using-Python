class Solution(object):
    def countBattleships(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == ".":
                return
            grid[r][c] = "."
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    dfs(i, j)
                    count += 1
        return count
        
        
