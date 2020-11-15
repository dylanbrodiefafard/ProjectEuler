from util.integers import aliquot_sum


def positive_integers():
    """The sequence of positive integers according to https://oeis.org/A000027"""
    n = 1
    while True:
        yield n
        n += 1


def triangle():
    n = 0
    while True:
        yield n * (n + 1) // 2
        n += 1


def square():
    n = 0
    while True:
        yield n ** 2
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


def heptagonal():
    n = 0
    while True:
        yield n * (5 * n - 3) // 2
        n += 1


def octagonal():
    n = 0
    while True:
        yield n * (3 * n - 2)
        n += 1


def spiral_diagonal():
    value = 3
    n = 1
    side_length = 3
    while True:
        yield value
        if n == 4:
            side_length += 2
            n = 1
        else:
            n += 1
        value += (side_length - 1)


def abundant():
    n = 12
    while True:
        if aliquot_sum(n) > n:
            yield n
        n += 1
