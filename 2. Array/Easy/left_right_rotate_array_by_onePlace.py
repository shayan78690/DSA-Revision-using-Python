arr = [1, 2, 3, 4, 5]
n = len(arr)
x = arr[0]
for i in range(0, n-1):
    arr[i] = arr[i+1]
arr[n-1] = x
print(arr)


arr = [1, 2, 3, 4, 5]
n = len(arr)
x = arr[n-1]  # store last element

for i in range(n-1, 0, -1):  # start from the end
    arr[i] = arr[i-1]        # shift elements to the right

arr[0] = x  # place last element at the start
print(arr)
