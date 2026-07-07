class Solution(object):
    def transpose(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        answer = [[0] * rows for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                answer[j][i] = matrix[i][j]

        return answer



