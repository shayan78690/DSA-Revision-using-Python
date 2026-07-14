class Solution(object):
    def bestTeamScore(self, scores, ages):
        # dp[i] means maximum team score ending with player i.
        n = len(scores)
        players = sorted(zip(ages, scores))
        dp = [0] * n
        for i in range(n):
            dp[i] = players[i][1]
        
        for index in range(n):
            for prevIndex in range(index):
                if players[index][1] >= players[prevIndex][1]:
                    dp[index] = max(dp[index], dp[prevIndex]+players[index][1])
        
        return max(dp)
