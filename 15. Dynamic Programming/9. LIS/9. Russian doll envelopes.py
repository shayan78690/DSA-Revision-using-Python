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



class Solution(object):
    def maxEnvelopes(self, envelopes):
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tail = []
        for width, height in envelopes:
            low = 0
            high = len(tail)-1
            while low <= high:
                mid = (low+high)//2
                if tail[mid] >= height:
                    high = mid-1
                else:
                    low = mid+1
            pos = low
            if pos == len(tail):
                tail.append(height)
            else:
                tail[pos] = height
        return len(tail)
