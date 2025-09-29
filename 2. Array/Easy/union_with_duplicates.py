class Solution:
    def findUnion(self, a, b):
        s = set()
        for i in a:
            s.add(i)
        for i in b:
            s.add(i)
        return sorted(list(s))   