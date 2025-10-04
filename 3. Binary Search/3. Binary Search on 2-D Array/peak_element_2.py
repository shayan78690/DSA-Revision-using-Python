class Solution(object):
    
    def func(self, mat, n, m, mid):
        maxi = -1
        idx = -1
        for i in range(n):
            if mat[i][mid] > maxi:
                maxi = mat[i][mid]
                idx = i
        return idx

    def findPeakGrid(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m-1
        while low <= high:
            mid = (low + high) // 2
            rowIdx = self.func(mat, n, m, mid)

            left = mat[rowIdx][mid-1] if mid-1 >= 0 else float('-inf')
            right = mat[rowIdx][mid+1] if mid+1 < m else float('-inf')

            if mat[rowIdx][mid] > left and mat[rowIdx][mid] > right:
                return [rowIdx, mid]
            elif left > mat[rowIdx][mid]:
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]

        