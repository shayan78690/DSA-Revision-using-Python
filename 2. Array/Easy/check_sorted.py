arr = [1, 2, 3, 4, 5]
n = len(arr)
ans = True
for i in range(1, n-1):
    if arr[i] < arr[i-1]:
        ans = False
print(ans)