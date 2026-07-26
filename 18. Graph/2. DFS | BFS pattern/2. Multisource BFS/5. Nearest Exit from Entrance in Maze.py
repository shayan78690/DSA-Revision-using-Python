from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1) and entrance != [r, c]:
                    return steps
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == ".":
                        maze[nr][nc] = "+"
                        q.append((nr, nc))
            steps += 1
        return -1
