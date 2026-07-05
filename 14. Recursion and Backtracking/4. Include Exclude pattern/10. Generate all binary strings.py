class Solution:
    def binstr(self, n):
        result = []
        self.func(n, "", result)
        return result
    def func(self, n, string, result):
        if n == 0:
            result.append(string)
            return
        self.func(n-1, string+"0", result)
        self.func(n-1, string+"1", result)
