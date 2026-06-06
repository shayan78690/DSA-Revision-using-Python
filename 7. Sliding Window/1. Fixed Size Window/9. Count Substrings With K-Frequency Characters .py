class Solution(object):
    def numberOfSubstrings(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        left = 0
        right = 0
        count = 0
        freq = {}
        while right < n:
            freq[s[right]] = freq.get(s[right], 0) + 1
            while freq[s[right]] == k:
                count += (n-right)
                freq[s[left]] -= 1
                left += 1
            right += 1
        return count
