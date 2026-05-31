class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)
        m = len(s2)
        if n > m:
            return False
        s1_freq = [0] * 26
        for i in range(n):
            s1_freq[ord(s1[i])-ord('a')] += 1
        
        window_freq = [0] * 26
        left = 0
        for right in range(m):
            window_freq[ord(s2[right])-ord('a')] += 1
            while right-left+1 > n:
                window_freq[ord(s2[left])-ord('a')] -= 1
                left += 1
            if right-left+1 == n:
                if window_freq == s1_freq:
                    return True
        return False
        
