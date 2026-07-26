from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        rows, cols = len(mat), len(mat[0])
        dis = [[-1] * cols for _ in range(rows)]
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    q.append((i, j)) 
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                new_row = dr + r
                new_col = dc + c
                if 0 <= new_row < rows and 0 <= new_col < cols and dis[new_row][new_col] == -1:
                    dis[new_row][new_col] = dis[r][c] + 1
                    q.append((new_row, new_col))
        return dis
        
