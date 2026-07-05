class Solution(object):
    def validStrings(self, n):
        result = []
        self.func(n, result, "", 0)
        return result
    def func(self, n, result, string, idx):
        if idx == n:
            result.append(string)
            return
        self.func(n, result, string+"1", idx+1)
        if not string or string[-1] != "0":
            self.func(n, result, string+"0", idx+1)
        
