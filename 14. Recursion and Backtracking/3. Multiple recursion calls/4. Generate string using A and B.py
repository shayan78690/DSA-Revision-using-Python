def generate(n, s):

    if n == 0:
        print(s)
        return

    generate(n-1, s + "A")

    generate(n-1, s + "B")
