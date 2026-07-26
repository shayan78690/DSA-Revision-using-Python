from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    image[nr][nc] == original
                ):
                    image[nr][nc] = color
                    queue.append((nr, nc))

        return image





from collections import deque
class Solution(object):

    def dfs(self, image, r, c, color, original_color, rows, cols):
        if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
            return
        image[r][c] = color
        
        self.dfs(image, r+1, c, color, original_color, rows, cols)
        self.dfs(image, r-1, c, color, original_color, rows, cols)
        self.dfs(image, r, c+1, color, original_color, rows, cols)
        self.dfs(image, r, c-1, color, original_color, rows, cols)

    def floodFill(self, image, sr, sc, color):
        rows = len(image)
        cols = len(image[0])
        original_color = image[sr][sc]
        if original_color == color:
            return image
        self.dfs(image, sr, sc, color, original_color, rows, cols)
        return image
