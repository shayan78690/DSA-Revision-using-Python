class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        count = [0] * 26
        left = 0
        right = 0
        max_length = 0
        max_freq = 0
        
        while right < n:
            count[ord(s[right]) - ord('A')] += 1
            max_freq = max(max_freq, count[ord(s[right]) - ord('A')])
            
            while (right - left + 1) - max_freq > k:
                count[ord(s[left]) - ord('A')] -= 1
                max_freq = max(count)
                left += 1
            
            if (right - left + 1) - max_freq <= k:
                max_length = max(max_length, right - left + 1)
            
            right += 1
        
        return max_length
