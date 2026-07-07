class Solution(object):
    def maximumWealth(self, accounts):
        n = len(accounts)
        m = len(accounts[0])
        maxi = 0
        for i in range(n):
            s = 0
            for j in range(m):
                s += accounts[i][j]
            maxi = max(maxi, s)
        return maxi
        
        
