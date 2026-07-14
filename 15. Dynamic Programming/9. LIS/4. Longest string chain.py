class Solution(object):

    def check(self, smallStr, largeStr):
        i = 0
        j = 0
        if len(largeStr) != len(smallStr) + 1:
            return False
        while i < len(smallStr) and j < len(largeStr):
            if smallStr[i] == largeStr[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i == len(smallStr)

    def longestStrChain(self, words):
        n = len(words)
        words.sort(key=len)
        dp = [1] * n
        for index in range(n):
            for prevIndex in range(index):
                if self.check(words[prevIndex], words[index]):
                    dp[index] = max(dp[index], dp[prevIndex]+1)
        return max(dp)
        
