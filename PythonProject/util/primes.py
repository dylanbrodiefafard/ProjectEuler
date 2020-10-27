from functools import lru_cache


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


@lru_cache
def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
