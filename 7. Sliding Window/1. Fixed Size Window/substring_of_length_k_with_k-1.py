class Solution:
    def substrCount(self, s, k):
        n = len(s)
        freq = {}
        count = 0
        left = 0
        right = 0
        for i in range(n):
            freq[s[right]] = freq.get(s[right], 0) + 1
            while right-left+1 > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            if right-left+1 == k and len(freq) == k-1:
                count += 1
            right += 1
        return count
        