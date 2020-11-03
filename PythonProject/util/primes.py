from itertools import takewhile, compress, islice, count, cycle


def primes():
    # Source: https://stackoverflow.com/a/3796442
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


def primes_up_to(n: int):
    yield 2
    assumed_primes = set(range(3, n + 1, 2))
    for maybe_prime in range(3, n + 1, 2):
        if maybe_prime not in assumed_primes:
            continue
        yield maybe_prime
        for multiple in range(maybe_prime ** 2, n + 1, 2 * maybe_prime):
            assumed_primes.discard(multiple)


_known_primes = {p: None for p in takewhile(lambda p: p < 1000, primes())}
_bases_by_limit = {
    2047: (2, ),
    1373653: (2, 3),
    9080191: (31, 73),
    25326001: (2, 3, 5),
    3215031751: (2, 3, 5, 7),
    4759123141: (2, 7, 61),
    1122004669633: (2, 13, 23, 1662803),
    2152302898747: (2, 3, 5, 7, 11),
    3474749660383: (2, 3, 5, 7, 11, 13),
    341550071728321: (2, 3, 5, 7, 11, 13, 17),
    3825123056546413051: (2, 3, 5, 7, 11, 13, 17, 19, 23),
    318665857834031151167461: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37),
    3317044064679887385961981: (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41),
}


def is_prime(n: int):
    # Source: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    # Updated with bases from: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Deterministic_variants
    if n in (0, 1):
        return False
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, r = n - 1, 0
    while not d % 2:
        d, r = d >> 1, r + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    for limit, bases in _bases_by_limit.items():
        if n >= limit:
            continue
        for a in bases:
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for i in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True
    raise ValueError(f'{n} is too large to determine primality with certainty.')
