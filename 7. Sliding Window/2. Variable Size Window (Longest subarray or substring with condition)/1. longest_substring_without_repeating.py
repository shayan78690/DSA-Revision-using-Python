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
    


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        while right < n:
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right-left+1)
            right += 1
        return max_len
