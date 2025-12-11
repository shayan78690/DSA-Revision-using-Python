class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(matrix[i][j])

        arr.sort()
        return arr[k - 1]
