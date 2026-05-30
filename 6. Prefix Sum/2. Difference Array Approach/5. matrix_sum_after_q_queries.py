class Solution(object):

    def setRow(self, mat, index, val):
        n = len(mat)
        for j in range(n):
            mat[index][j] = val
    
    def setCol(self, mat, index, val):
        n = len(mat)
        for i in range(n):
            mat[i][index] = val

    def matrixSumQueries(self, n, queries):
        mat = [[0] * n for _ in range(n)]
        for query in queries:
            type_ = query[0]
            index = query[1]
            val = query[2]
            if type_ == 0:
                self.setRow(mat, index, val)
            if type_ == 1:
                self.setCol(mat, index, val)
        
        total = 0
        for i in range(n):
            for j in range(n):
                total += mat[i][j]
        return total
        
