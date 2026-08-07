class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return []
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        result = []
        directions = [(-1, 0, "U"), (1, 0, "D"), (0, -1, "L"), (0, 1, "R")]
        self.solve(maze, n, 0, 0, result, [], visited, directions)
        result.sort()
        return result

    def solve(self, maze, n, r, c, result, path, visited, directions):
        if r == n - 1 and c == n - 1:
            result.append("".join(path))
            return
        for dr, dc, ch in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < n and
                0 <= nc < n and
                maze[nr][nc] == 1 and
                not visited[nr][nc]):
                visited[nr][nc] = True
                path.append(ch)
                self.solve(maze, n, nr, nc, result, path, visited, directions)
                path.pop()
                visited[nr][nc] = False
