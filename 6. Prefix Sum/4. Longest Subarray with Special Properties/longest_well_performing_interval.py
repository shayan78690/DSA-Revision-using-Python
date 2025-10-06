class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        n = len(hours)
        max_len = 0
        score = 0
        m = {}
        m[0] = -1
        for i in range(n):
            if hours[i] > 8:
                score += 1
            else:
                score -=1

            if score > 0:
                max_len = i+1
            else:
                if (score-1) in m:
                    max_len = max(max_len, i-m[score-1])
            if score not in m:
                m[score] = i
        return max_len
        