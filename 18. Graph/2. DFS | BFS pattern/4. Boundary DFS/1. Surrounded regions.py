class Solution(object):

    def dfs(self, board, rows, cols, r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
            return
        board[r][c] = "S"
        self.dfs(board, rows, cols, r+1, c)
        self.dfs(board, rows, cols, r-1, c)
        self.dfs(board, rows, cols, r, c+1)
        self.dfs(board, rows, cols, r, c-1)

    def solve(self, board):
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            if board[r][0] == "O":
                self.dfs(board, rows, cols, r, 0)
            if board[r][cols-1] == "O":
                self.dfs(board, rows, cols, r, cols-1)
        
        for c in range(cols):
            if board[0][c] == "O":
                self.dfs(board, rows, cols, 0, c)
            if board[rows-1][c] == "O":
                self.dfs(board, rows, cols, rows-1, c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

        
from collections import deque
class Solution(object):

    def add(self, board, rows, cols, r, c, q):
        board[r][c] = "S"
        q.append((r, c))

    def solve(self, board):
        rows, cols = len(board), len(board[0])
        q = deque()
        for r in range(rows):
            if board[r][0] == "O":
                self.add(board, rows, cols, r, 0, q)
            if board[r][cols-1] == "O":
                self.add(board, rows, cols, r, cols-1, q)
        
        for c in range(cols):
            if board[0][c] == "O":
                self.add(board, rows, cols, 0, c, q)
            if board[rows-1][c] == "O":
                self.add(board, rows, cols, rows-1, c, q)
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "O":
                    self.add(board, rows, cols, nr, nc, q)
        

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

        
        

