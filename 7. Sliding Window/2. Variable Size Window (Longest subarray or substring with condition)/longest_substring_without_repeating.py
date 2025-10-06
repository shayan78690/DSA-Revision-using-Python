class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxi = 0
        for i in range(0, n):
            st = set()
            for j in range(i, n):
                ch = s[j]
                if ch in st:
                    break
                st.add(ch)
                maxi = max(maxi, j-i+1)

        return maxi


class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxi = 0
        left = 0
        right = 0
        freq = {}
        while right < n:
            freq[s[right]] = freq.get(s[right], 0)+1
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            maxi = max(maxi, right-left+1)
            right += 1
        return maxi
    


class Solution2(object):
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