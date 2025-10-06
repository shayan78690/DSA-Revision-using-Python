class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        freq = [0] * 3
        left = 0
        right = 0
        count = 0
        
        while right < n:
            ch = s[right]
            freq[ord(ch) - ord('a')] += 1
            
            while freq[0] >= 1 and freq[1] >= 1 and freq[2] >= 1:
                count += (n - right)
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1
            
            right += 1
        
        return count