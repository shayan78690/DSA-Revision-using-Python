class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        hashset = set(wordDict)
        return self.func(s, n, hashset, 0)
    
    def func(self, s, n, hashset, start):
        if start == n:
            return True
        for end in range(start, n):
            part = s[start:end+1]
            if part in hashset:
                if self.func(s, n, hashset, end+1):
                    return True
        return False
        
