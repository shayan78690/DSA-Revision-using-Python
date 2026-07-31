class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        du = self.find(u)
        dv = self.find(v)
        if du == dv:
            return
        if self.size[du] < self.size[dv]:
            du, dv = dv, du
        self.parent[dv] = du
        self.size[du] += self.size[dv]

class Solution(object):
    def removeStones(self, stones):
        totalStones = len(stones)
        maxRow = maxCol = 0
        for r, c in stones:
            maxRow = max(maxRow, r)
            maxCol = max(maxCol, c)
        
        nodes = set()
        dsu = DSU(maxRow+maxCol+2)
        for r, c in stones:
            rowNode = r
            colNode = c + maxRow + 1
            dsu.union(rowNode, colNode)
            nodes.add(rowNode)
            nodes.add(colNode)
        
        components = 0
        for node in nodes:
            if dsu.find(node) == node:
                components += 1
        return totalStones - components
        
        
