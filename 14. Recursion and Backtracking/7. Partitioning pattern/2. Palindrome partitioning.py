class Solution(object):
    def partition(self, s):
        n = len(s)
        result = []
        self.func(s, n, result, [], 0)
        return result
    
    def func(self, s, n, result, current, start):
        if start == n:
            result.append(current[:])
            return
        for end in range(start, n):
            substring = s[start:end+1]
            if self.palindrome(substring):
                current.append(substring)
                self.func(s, n, result, current, end+1)
                current.pop()
    
    def palindrome(self, string):
        return string == string[::-1]



def func(s, n, result, current, start):
    if start == n:
        result.append(current[:])
        return
    for end in range(start, n):
        current.append(s[start:end+1])
        func(s, n, result, current, end+1)
        current.pop()

s = input()
result = []
func(s, len(s), result, [], 0)
print(result)
