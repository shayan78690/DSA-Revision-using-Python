class Solution:
    def longestKSubstr(self, s, k):
        # code here
        map = {}
        n = len(s)
        left = 0
        right = 0
        maxLen = -1
        
        while right < n:
            ch = s[right]
            map[ch] = map.get(ch, 0) + 1
            
            while len(map) > k:
                c = s[left]
                map[c] = map[c] - 1
                if map[c] == 0:
                    del map[c]
                left += 1
            
            if len(map) == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
        
        return maxLen
        
        