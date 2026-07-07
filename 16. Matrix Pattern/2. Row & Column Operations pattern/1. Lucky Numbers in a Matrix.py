class Solution(object):
    def luckyNumbers(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        result = []
        for i in range(n):
            col = 0
            mini = matrix[i][0]
            for j in range(1, m):
                if mini > matrix[i][j]:
                    mini = matrix[i][j]
                    col = j
            lucky = True
            for k in range(n):
                if matrix[k][col] > mini:
                    lucky = False
                    break
            if lucky:
                result.append(mini)
        return result
        
