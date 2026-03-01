import math
L = 2
R = 20
prime = [0] * (R+1)
for i in range(2, R+1):
    prime[i] = 1

for i in range(2, int(math.sqrt(R)) + 1):
    if prime[i] == 1:
        for j in range(i*i, R+1, i):
            prime[j] = 0

count = 0
for i in range(L, R+1):
    if prime[i] == 1:
        count += 1
print(count)ac




import math
class Solution:
    def countPrimes(self,L,R):
        isPrime = [0] * (R+1)
        for i in range(2, R+1):
            isPrime[i] = 1
        
        for i in range(2, int(math.sqrt(R))+1):
            if isPrime[i] == 1:
                for j in range(i*i, R+1, i):
                    isPrime[j] = 0
        
        
        count = 0
        for i in range(L, R+1):
            if isPrime[i] == 1:
                count += 1
        
        return count
        
