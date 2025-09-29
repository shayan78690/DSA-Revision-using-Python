arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)
k = k % n
temp = []
for i in range(0, k):
    temp.append(arr[i])
print(temp)

for i in range(0, (n-k)):
    arr[i] = arr[i+k]

for i in range(n-k, n):
    arr[i] = temp[i-n+k]
print(arr)







arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)
k = k % n
temp = []

for i in range(n-k, n):
    temp.append(arr[i])
print(temp)

for i in range(n-k-1, -1, -1):
    arr[i+k] = arr[i]
print(arr)

for i in range(0, k):
    arr[i] = temp[i]
    
print(arr)




def reverse(arr, start, end):
    while start <= end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        
        start += 1
        end -= 1

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
n = len(arr)
k = k % n

reverse(arr, 0, k-1)
reverse(arr, k, n-1)
reverse(arr, 0, n-1)
print(arr)






class Solution(object):
    def reverse(self, arr, start, end):
        while start <= end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
        
            start += 1
            end -= 1
        
    def rotate(self, arr, k):
        n = len(arr)
        k = k % n
        self.reverse(arr, 0, n-k-1)  
        self.reverse(arr, n-k, n-1)
        self.reverse(arr, 0, n-1)
    