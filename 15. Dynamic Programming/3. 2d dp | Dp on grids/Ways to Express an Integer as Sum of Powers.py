class Solution(object):
    def numberOfWays(self, n, x):
        mod = 10**9+7
        return self.func(n, x, 1) % mod
        
    def func(self, n, x, number):
        if n == 0:
            return 1
        if number**x > n:
            return 0
        take = self.func(n-number**x, x, number+1)
        skip = self.func(n, x, number+1)
        return take+skip
        
