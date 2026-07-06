class Solution(object):
    def wordBreak(self, s, wordDict):
        n = len(s)
        words = set(wordDict)
        result = []
        self.func(s, n, result, [], 0, words)
        return result
    
    def func(self, s, n, result, current, start, words):
        if start == n:
            result.append(" ".join(current[:]))
            return
        for end in range(start, n):
            part = s[start:end+1]
            if part in words:
                current.append(part)
                self.func(s, n, result, current, end+1, words)
                current.pop()
        
