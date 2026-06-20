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


import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        maxheap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(maxheap, -matrix[i][j])
                if len(maxheap) > k:
                    heapq.heappop(maxheap)
        return -maxheap[0]

        
