from collections import deque
import heapq

class Solution(object):
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        maxHeap = []
        heapq.heappush(maxHeap, (-dist[0][0], 0, 0))

        best = [[-1] * n for _ in range(n)]
        best[0][0] = dist[0][0]

        while maxHeap:
            safe, r, c = heapq.heappop(maxHeap)
            safe = -safe

            if (r, c) == (n - 1, n - 1):
                return safe

            if safe < best[r][c]:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    newSafe = min(safe, dist[nr][nc])

                    if newSafe > best[nr][nc]:
                        best[nr][nc] = newSafe
                        heapq.heappush(maxHeap, (-newSafe, nr, nc))
