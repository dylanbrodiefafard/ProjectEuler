def triangular():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1


def pentagonal():
    n = 0
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def hexagonal():
    n = 0
    while True:
        yield n * (2 * n - 1)
        n += 1
