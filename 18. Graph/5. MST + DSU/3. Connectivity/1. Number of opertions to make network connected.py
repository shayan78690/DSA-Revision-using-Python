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
    def makeConnected(self, n, connections):
        if len(connections) < n-1:
            return -1
        dsu = DSU(n)
        for u, v in connections:
            if dsu.union(u, v):
                n -= 1
        return n-1


