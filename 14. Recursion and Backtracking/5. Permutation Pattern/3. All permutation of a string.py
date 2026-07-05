class Solution:
    def permutation(self, s):
        n = len(s)
        result = []
        visited = [False] * n
        self.func(s, n, result, [], visited)
        return result
    
    def func(self, s, n, result, current, visited):
        if len(current) == n:
            string = "".join(current)
            result.append(string)
            return
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            current.append(s[i])
            self.func(s, n, result, current, visited)
            visited[i] = False
            current.pop()
            
