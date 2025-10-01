class Solution(object):
    def nCr(self, n, r):
        res = 1
        for i in range(r):
            res = res * (n-i)
            res = res // (i+1)
        return res

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        for c in range(0, rowIndex+1):
            ans.append(self.nCr(rowIndex, c))
        return ans



class Solution1:
    
    def func(self, rowIndex, ans):
        res = 1
        ans.append(res)
        for i in range(1, rowIndex):
            res = res * (rowIndex-i)
            res = res // i
            ans.append(res)
        return ans
    
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = []
        self.func(rowIndex+1, ans)
        return ans

        