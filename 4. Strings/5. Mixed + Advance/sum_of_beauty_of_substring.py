class Solution(object):
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        total = 0
        for i in range(n):
            freq = {}
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1
                values = [v for v in freq.values() if v > 0]
                maxi = max(values)
                mini = min(values)
                total += (maxi - mini)
        return total
