class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        return True
from typing import List
class Solution:
    def numOfIslands(self, rows: int, cols : int, operators : List[List[int]]) -> List[int]:
        grid = [[0] * cols for _ in range(rows)]
        dsu = DSU(rows*cols)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        ans = []
        for r, c in operators:
            if grid[r][c] == 1:
                ans.append(count)
                continue
            grid[r][c] = 1
            count += 1
            node = r*cols+c
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    adjNode = nr*cols+nc
                    if dsu.union(node, adjNode):
                        count -= 1
            ans.append(count)
        return ans
