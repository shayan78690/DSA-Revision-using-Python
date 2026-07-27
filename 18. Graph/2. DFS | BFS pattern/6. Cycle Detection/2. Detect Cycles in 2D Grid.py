class Solution(object):
    def containsCycle(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(i, j, pi, pj):
            visited[i][j] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = i + dr
                nc = j + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if grid[i][j] == grid[nr][nc]:
                        if not visited[nr][nc]:
                            if dfs(nr, nc, i, j):
                                return True
                        elif (nr, nc) != (pi, pj):
                            return True
            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True
        return False




from collections import deque
class Solution(object):
    def containsCycle(self, grid):
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            q = deque()
            q.append((i, j, -1, -1))
            visited[i][j] = True
            while q:
                r, c, pr, pc = q.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[r][c] == grid[nr][nc]:
                        if not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc, r, c))
                        elif (nr, nc) != (pr, pc):
                            return True
            return False

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if bfs(i, j):
                        return True
        return False
        
