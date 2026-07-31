class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1] * (n+1)
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
    def maxNumEdgesToRemove(self, n, edges):
        dsu1 = DSU(n)
        dsu2 = DSU(n)
        removed = 0
        n1 = n2 = n
        edges.sort(reverse=True)
        for t, u, v in edges:
            if t == 3:
                if dsu1.union(u, v):
                    dsu2.union(u, v)
                    n1 -= 1
                    n2 -= 1
                else:
                    removed += 1
            elif t == 1:
                if dsu1.union(u, v):
                    n1 -= 1
                else:
                    removed += 1
            else:
                if dsu2.union(u, v):
                    n2 -= 1
                else:
                    removed += 1
        return removed if n1 == 1 and n2 == 1 else -1
        
        
