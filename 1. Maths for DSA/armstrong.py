class Solution:
    def armstrongNumber (self, n):
        num = n
        armstrong = 0
        while num != 0:
            ld = num % 10
            armstrong += ld**3
            num = num // 10
        return armstrong == n