from typing import List
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
class Solution:
    def kruskalsMST(self, V: int, edges: List[List[int]]) -> int:
        edges.sort(key = lambda x : x[2])
        dsu = DSU(V)
        mstWeight = 0
        for u, v, w in edges:
            if dsu.union(u, v):
                mstWeight += w
        return mstWeight
