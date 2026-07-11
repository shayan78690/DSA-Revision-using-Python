class Solution(object):
    def minDistance(self, word1, word2):
        return self.func(word1, word2, 0, 0)
    
    def func(self, word1, word2, i, j):
        if i == len(word1):
            return len(word2)-j
        if j == len(word2):
            return len(word1)-i
        if word1[i] == word2[j]:
            return self.func(word1, word2, i+1, j+1)
        insert  = 1 + self.func(word1, word2, i, j+1)
        delete = 1 + self.func(word1, word2, i+1, j)
        replace = 1 + self.func(word1, word2, i+1, j+1)

        return min(insert, delete, replace)

  class Solution(object):
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[-1] * m for _ in range(n)]
        return self.func(word1, word2, 0, 0, dp)
    
    def func(self, word1, word2, i, j, dp):
        if i == len(word1):
            return len(word2)-j
        if j == len(word2):
            return len(word1)-i
        if dp[i][j] != -1:
            return dp[i][j]
        if word1[i] == word2[j]:
            dp[i][j] = self.func(word1, word2, i+1, j+1, dp)
        else:
            insert  = 1 + self.func(word1, word2, i, j+1, dp)
            delete = 1 + self.func(word1, word2, i+1, j, dp)
            replace = 1 + self.func(word1, word2, i+1, j+1, dp)
            dp[i][j] = min(insert, delete, replace)
        return dp[i][j]


class Solution(object):
    def minDistance(self, word1, word2):
        n, m = len(word1), len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[n][j] = m-j
        for i in range(n+1):
            dp[i][m] = n-i
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    insert  = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, delete, replace)
        return dp[0][0]
