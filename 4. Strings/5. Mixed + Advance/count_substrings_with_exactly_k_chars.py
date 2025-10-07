class Solution:
    def countSubstr (self, s, k):
        return self.func(s, k) - self.func(s, k-1)
    
    def func(self, s, k):
        if k < 0 :
            return 0
        left = 0
        right = 0
        count = 0
        freq = {}
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            
            while len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            count += right-left+1
            right += 1
        return count