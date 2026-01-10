class Solution:
    def power(self, x: int, n: int) -> int:
        if n == 0:
            return 1

        half = self.power(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return x * half * half
