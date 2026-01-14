class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        maxi = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                maxi = max(maxi, j-i+1)
        return maxi 
        



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
