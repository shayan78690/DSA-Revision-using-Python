class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])

        chainLen = 1
        chainEnd = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > chainEnd:
                chainLen += 1
                chainEnd = pairs[i][1]

        return chainLen
