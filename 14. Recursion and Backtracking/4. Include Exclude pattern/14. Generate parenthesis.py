class Solution(object):
    def generateParenthesis(self, n):
        result = []
        self.func(n, result, "", 0, 0, 0)
        return result
    def func(self, n, result, string, open, close, idx):
        if idx == 2*n:
            result.append(string)
            return
        if open < n:
            self.func(n, result, string+"(", open+1, close, idx+1)
        if close < open:
            self.func(n, result, string+")", open, close+1, idx+1)
        
