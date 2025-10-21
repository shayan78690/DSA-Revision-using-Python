class Solution:
    def tilingProblem(self, n):
        if n == 0 or n == 1:
            return 1

        fnm1 = self.tilingProblem(n - 1)
        fnm2 = self.tilingProblem(n - 2)
        totalWays = fnm1 + fnm2
        return totalWays
