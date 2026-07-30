class DSU:
    def  __init__(self, n):
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
    def accountsMerge(self, accounts):
        n = len(accounts)
        dsu = DSU(n)
        accountMapping = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in accountMapping:
                    accountMapping[email] = i
                else:
                    dsu.union(i, accountMapping[email])
        
        merged = {} # parent -> email
        for email, account in accountMapping.items():
            parent = dsu.find(account)
            if parent not in merged:
                merged[parent] = []
            merged[parent].append(email)
        ans = []
        for parent, emails in merged.items():
            ans.append([accounts[parent][0]] + sorted(emails))
        return ans
