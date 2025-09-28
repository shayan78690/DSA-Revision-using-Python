class Solution:
    def print_divisors(self, N):
        for i in range(1, N+1):
            if N % i == 0:
                print(i, end=" ")
                