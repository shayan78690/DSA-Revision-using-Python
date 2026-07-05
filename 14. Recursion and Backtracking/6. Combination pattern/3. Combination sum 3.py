class Solution(object):
    def combinationSum3(self, k, n):
        result = []
        self.func(k, n, result, [], 1)
        return result
    
    def func(self, k, n, result, current, start):
        if len(current) == k and n == 0:
            result.append(current[:])
            return
        if len(current) > k or n < 0:
            return
        for i in range(start, 10):
            current.append(i)
            self.func(k, n-i, result, current, i+1)
            current.pop()
        
