# when width are equal sort height in descending order
class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)

        dp = [1] * n

        for index in range(n):
            for prevIndex in range(index):

                if (envelopes[index][0] > envelopes[prevIndex][0] and
                    envelopes[index][1] > envelopes[prevIndex][1]):

                    dp[index] = max(dp[index], dp[prevIndex] + 1)

        return max(dp)
