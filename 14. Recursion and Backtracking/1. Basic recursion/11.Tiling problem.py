def tile(n):
    if n == 0 or n == 1:
        return 1

    vertical = tile(n - 1)
    horizontal = tile(n - 2)

    return vertical + horizontal
