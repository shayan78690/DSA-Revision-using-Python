n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
print(matrix)


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(matrix)


n = int(input())
matrix = [list(map(int, input().split(","))) for _ in range(n)]
print(matrix)

