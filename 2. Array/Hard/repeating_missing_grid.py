class Solution:
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        missing = -1
        repeating = -1
        s = set()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] in s:
                    repeating = grid[i][j]
                else:
                    s.add(grid[i][j])
        
        for i in range(1, n*n+1):
            if i not in s:
                missing = i
        return [repeating, missing]

        