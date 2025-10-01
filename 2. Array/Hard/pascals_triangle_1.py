def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return res

r = 5
c = 3
element = nCr(r-1, c-1)
print(element)    