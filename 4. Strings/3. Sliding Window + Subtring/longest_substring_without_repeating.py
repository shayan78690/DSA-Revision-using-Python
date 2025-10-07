class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        left = 0
        right = 0
        maxi = 0
        freq = {}
        while right < n:
            if s[right] in freq:
                left = max(left, freq[s[right]]+1)
            freq[s[right]] = right
            maxi = max(maxi, right-left+1)
            right += 1
        return maxi