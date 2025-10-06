class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        n = len(gain)
        highest = 0
        prefix = [0] * (n + 1)
        prefix[0] = 0

        for i in range(1, n + 1):
            prefix[i] = gain[i - 1] + prefix[i - 1]
            highest = max(highest, prefix[i])

        return highest