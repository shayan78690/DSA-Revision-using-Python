import math
class Solution:
    def func(self, n):
        result = []
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0:
                result.append(i)
                if i != n // i:
                    result.append(n//i)
        return result


n = int(input())
obj = Solution()
result = obj.func(n)
print(result)
