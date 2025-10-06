class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        prefix = [[0] * m for i in range(n)]
        prefix[0][0] = mat[0][0]
        for j in range(1, m):
            prefix[0][j] = prefix[0][j-1] + mat[0][j]
        for i in range(1, n):
            prefix[i][0] = prefix[i-1][0] + mat[i][0]

        for i in range(1, n):
            for j in range(1, m):
                prefix[i][j] = mat[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        ans = [[0] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                r1 = max(0, i-k)
                r2 = min(n-1, i+k)
                c1 = max(0, j-k)
                c2 = min(m-1, j+k)
                total = prefix[r2][c2]
                left = prefix[r2][c1-1] if c1 != 0 else 0
                top = prefix[r1-1][c2] if r1 != 0 else 0
                topleft = prefix[r1-1][c1-1] if (r1 != 0 and c1 != 0) else 0
                extra = left+top-topleft
                ans[i][j] = total - extra

        return ans