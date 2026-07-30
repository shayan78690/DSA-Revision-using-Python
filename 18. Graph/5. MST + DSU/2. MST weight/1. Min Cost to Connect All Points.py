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

class Solution(object):
    def minCostConnectPoints(self, points):
        n = len(points)
        edges = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append([cost, i, j])
        edges.sort()
        dsu = DSU(n)
        mstWeight = 0
        edges_used = 0
        for cost, u, v in edges:
            if dsu.union(u, v):
                mstWeight += cost
                edges_used += 1
            if edges_used == n-1:
                break
        return mstWeight
