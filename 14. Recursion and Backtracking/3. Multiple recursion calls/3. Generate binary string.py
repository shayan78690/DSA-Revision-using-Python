def binary(n, ans):

    if n == 0:
        print(ans)
        return

    binary(n-1, ans + "0")

    binary(n-1, ans + "1")
