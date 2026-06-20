import heapq

class Row:
    def __init__(self, count, idx):
        self.count = count   
        self.idx = idx       
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.idx < other.idx
        return self.count < other.count

class Solution(object):
    def kWeakestRows(self, mat, k):
        n = len(mat)
        m = len(mat[0])

        pq = [] 

        for i in range(n):
            count = 0
            for j in range(m):
                if mat[i][j] == 1:
                    count += 1
                else:
                    continue
            heapq.heappush(pq, Row(count, i))

        ans = []
        for _ in range(k):
            r = heapq.heappop(pq)
            ans.append(r.idx)

        return ans





