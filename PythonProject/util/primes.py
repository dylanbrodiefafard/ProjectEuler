from itertools import takewhile


def primes():
    """
    Generate an infinite sequence of prime numbers.
    Sieve of Eratosthenes
    Code by David Eppstein, UC Irvine, 28 Feb 2002
    http://code.activestate.com/recipes/117119/

    Maps composites to primes witnessing their compositeness.
    This is memory efficient, as the sieve is not "run forward"
    indefinitely, but only as long as required by the current
    number being tested.
    """
    divisors = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in divisors:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            divisors[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in divisors[q]:
                divisors.setdefault(p + q, []).append(p)
            del divisors[q]

        q += 1


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
