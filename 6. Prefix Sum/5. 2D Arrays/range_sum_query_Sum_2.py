class NumMatrix(object):
    
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        self.prefix = [[0] * m for _ in range(n)]
        self.prefix[0][0] = matrix[0][0]
        for j in range(1, m):
            self.prefix[0][j] = matrix[0][j] + self.prefix[0][j-1]
        for i in range(1, n):
            self.prefix[i][0] = matrix[i][0] + self.prefix[i-1][0]
        
        for i in range(1, n):
            for j in range(1, m):
                self.prefix[i][j] = matrix[i][j] + self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = self.prefix[row2][col2]
        left = self.prefix[row2][col1-1] if col1 != 0 else 0
        top = self.prefix[row1-1][col2] if row1 != 0 else 0
        topleft = self.prefix[row1-1][col1-1] if (row1 != 0 and col1 != 0) else 0
        return total - (left + top - topleft)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)