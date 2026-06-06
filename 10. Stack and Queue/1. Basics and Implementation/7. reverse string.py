s = input()
stack = []
for ch in s:
    stack.append(ch)
result = []
while stack:
    result.append(stack.pop())
result = "".join(result)
print(result)
