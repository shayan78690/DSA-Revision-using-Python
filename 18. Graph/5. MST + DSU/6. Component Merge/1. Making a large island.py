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
            return
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = self.parent[pu]
        self.size[pu] += self.size[pv]
class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        dsu = DSU(n*n)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                node = r*n+c
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    adjNode = nr*n+nc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        dsu.union(node, adjNode)
        ans = 0
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    continue
                node = r*n+c
                parents = set()
                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    adjNode = nr*n+nc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                        pt = dsu.find(adjNode)
                        parents.add(pt)
                size = 1
                for parent in parents:
                    size += dsu.size[parent]
                ans = max(ans, size)

        for i in range(n*n):
            if dsu.find(i) == i:
                ans = max(ans, dsu.size[i])
        return ans        
