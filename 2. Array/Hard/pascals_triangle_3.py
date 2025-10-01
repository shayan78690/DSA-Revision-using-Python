class Solution:
    def nCr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i+1)
        return res
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(1, numRows+1):
            temp = []
            for col in range(1, row+1):
                temp.append(self.nCr(row-1, col-1))
            ans.append(temp)
        return ans



class Solution1:
    
    def generateRow(self, n):
        res = 1
        temp = []
        temp.append(res)
        for i in range(1, n):
            res = res * (n-i)
            res = res // i
            temp.append(res)
        return temp


    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for row in range(1, numRows+1):
            ans.append(self.generateRow(row))
        return ans
        