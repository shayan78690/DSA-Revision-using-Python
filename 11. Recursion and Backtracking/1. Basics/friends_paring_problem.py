class Solution:
    def friendsPairingProblem(self, n):
        if n == 1 or n == 2:
            return n

        fnm1 = self.friendsPairingProblem(n - 1)  # single friend
        fnm2 = self.friendsPairingProblem(n - 2)  # pair up one friend
        pairWays = (n - 1) * fnm2
        totalWays = fnm1 + pairWays

        return totalWays
