class Solution(object):
    def combine(self, n, k):
        result = []
        self.func(n, k, result, [], 1)
        return result
    
    def func(self, n, k, result, current, start):
        if len(current) == k:
            result.append(current[:])
            return
        if len(current) > k:
            return
        for i in range(start, n+1):
            current.append(i)
            self.func(n, k, result, current, i+1)
            current.pop()
        
