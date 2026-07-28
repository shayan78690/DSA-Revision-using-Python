from collections import deque
class Solution:
    def shortestPath(self, mat: list[list[int]], src: list[int], dest: list[int]) -> int:
        n, m = len(mat), len(mat[0])
        sr, sc = src
        dr, dc = dest
        if mat[sr][sc] == 0 or mat[dr][dc] == 0:
            return -1
        if src == dest:
            return 0
        dist = [[float('inf')] * m for _ in range(n)]
        dist[sr][sc] = 0
        q = deque()
        q.append((sr, sc))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c = q.popleft()
            if [r, c] == dest:
                return dist[r][c]
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0 <= nr < n and 0 <= nc < m and mat[nr][nc] == 1 and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        return -1
