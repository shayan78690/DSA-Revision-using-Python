from collections import defaultdict

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

        self.parent[pv] = pu
        self.size[pu] += self.size[pv]


class Solution(object):
    def countCompleteComponents(self, n, edges):
        dsu = DSU(n)

        for u, v in edges:
            dsu.union(u, v)

        edgeCount = defaultdict(int)

        for u, v in edges:
            parent = dsu.find(u)
            edgeCount[parent] += 1

        ans = 0

        for i in range(n):
            if dsu.find(i) != i:
                continue

            nodes = dsu.size[i]
            requiredEdges = nodes * (nodes - 1) // 2

            if edgeCount[i] == requiredEdges:
                ans += 1

        return ans
