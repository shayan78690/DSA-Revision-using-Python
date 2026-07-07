class Solution(object):
    def numSpecial(self, mat):
        n, m = len(mat), len(mat[0])

        row_count = [0]*n
        col_count = [0]*m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        count = 0

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    count += 1

        return count
