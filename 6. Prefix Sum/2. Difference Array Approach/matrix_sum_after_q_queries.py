class Solution(object):
    def matrixSumQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: int
        """
        row_seen_count = 0
        col_seen_count = 0
        rowIndex = [False] * n
        colIndex = [False] * n
        total_sum = 0
        for i in range(len(queries)-1, -1, -1):
            type_ = queries[i][0]
            index = queries[i][1]
            val = queries[i][2]

            if type_ == 0 and not rowIndex[index]:
                row_seen_count += 1
                rowIndex[index] = True
                total_sum += (n - col_seen_count) * val
            elif type_ == 1 and not colIndex[index]:
                col_seen_count += 1
                colIndex[index] = True
                total_sum += (n - row_seen_count) * val
        return total_sum


            