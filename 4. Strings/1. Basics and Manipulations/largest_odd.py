class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        n = len(num)
        for i in range(n-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]
        return ""