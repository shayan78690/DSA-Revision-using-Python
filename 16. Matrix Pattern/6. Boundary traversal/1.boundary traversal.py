class Solution:
    def boundaryTraversal(self, mat):
        n, m = len(mat), len(mat[0])

        top, bottom = 0, n - 1
        left, right = 0, m - 1

        result = []

        for j in range(left, right + 1):
            result.append(mat[top][j])

        for i in range(top + 1, bottom + 1):
            result.append(mat[i][right])

        if top != bottom:
            for j in range(right - 1, left - 1, -1):
                result.append(mat[bottom][j])

        if left != right:
            for i in range(bottom - 1, top, -1):
                result.append(mat[i][left])

        return result
