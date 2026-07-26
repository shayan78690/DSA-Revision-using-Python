from collections import deque

class Solution:
    def highestPeak(self, isWater):
        rows = len(isWater)
        cols = len(isWater[0])

        queue = deque()
        height = [[-1] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if isWater[r][c] == 1:
                    height[r][c] = 0
                    queue.append((r, c))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    height[nr][nc] == -1
                ):
                    height[nr][nc] = height[r][c] + 1
                    queue.append((nr, nc))

        return height
