class Solution:
    def func(self, x, n):
        if n == 0:
            return 1
        half = self.func(x, n//2)
        return half*half if n % 2 == 0 else x*half*half

x, n = map(int, input().split(" "))
obj = Solution()
result = obj.func(x, n)
print(result)
