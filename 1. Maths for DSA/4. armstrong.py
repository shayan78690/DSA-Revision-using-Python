class Solution:
    def armstrongNumber(self, n):
        digits = self.countDigits(n)
        num = n
        armstrong = 0

        while num > 0:
            ld = num % 10
            armstrong += ld ** digits
            num //= 10

        return armstrong == n

    def countDigits(self, n):
        if n == 0:
            return 1
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count
