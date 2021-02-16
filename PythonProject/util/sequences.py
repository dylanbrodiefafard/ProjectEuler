from itertools import compress, islice, count, cycle

from util.integers import aliquot_sum


def positive_integers():
    """
    https://oeis.org/A000027
    """
    n = 1
    while True:
        yield n
        n += 1


def triangular_numbers(n=None):
    """
    https://oeis.org/A000217
    """
    if n is None:
        n = 0
    assert n >= 0, 'Index must be a positive integer.'
    while True:
        yield n * (n + 1) // 2
        n += 1


def squares():
    """
    https://oeis.org/A000290
    """
    n = 0
    while True:
        yield n ** 2
        n += 1


def pentagonal_numbers():
    """
    https://oeis.org/A000326
    """
    n = 0
    while True:
        yield n * (3 * n - 1) // 2
        n += 1


def hexagonal_numbers():
    """
    https://oeis.org/A000384
    """
    n = 0
    while True:
        yield n * (2 * n - 1)
        n += 1


def heptagonal_numbers():
    """
    https://oeis.org/A000566
    """
    n = 0
    while True:
        yield n * (5 * n - 3) // 2
        n += 1


def octagonal_numbers():
    """
    https://oeis.org/A000567
    """
    n = 0
    while True:
        yield n * (3 * n - 2)
        n += 1


def ulams_spiral_diagonal_numbers():
    """
    https://oeis.org/A200975
    """
    yield 1
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


def abundant_numbers():
    """
    https://oeis.org/A005101
    """
    n = 12
    while True:
        if aliquot_sum(n) > n:
            yield n
        n += 1


def prime_numbers():
    """
    https://oeis.org/A000040
    reference: https://stackoverflow.com/a/3796442
    """
    yield from [2, 3, 5]

    divisors = {9: 3, 25: 5}
    mask = (1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0)
    modulos = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

    for q in compress(islice(count(7), 0, None, 2), cycle(mask)):
        p = divisors.pop(q, None)
        if p is None:
            divisors[q * q] = q
            yield q
        else:
            x = q + 2 * p
            while x in divisors or (x % 30) not in modulos:
                x += 2 * p
            divisors[x] = p


def prime_numbers_up_to(n):
    """
    https://oeis.org/A000040
    """
    yield 2
    assumed_primes = set(range(3, n + 1, 2))
    for maybe_prime in range(3, n + 1, 2):
        if maybe_prime not in assumed_primes:
            continue
        yield maybe_prime
        for multiple in range(maybe_prime ** 2, n + 1, 2 * maybe_prime):
            assumed_primes.discard(multiple)
