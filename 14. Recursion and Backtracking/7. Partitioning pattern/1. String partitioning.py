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
