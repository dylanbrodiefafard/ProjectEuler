import itertools
from collections import Counter, deque
from functools import reduce, total_ordering
from math import gcd, isqrt, comb

from util.more_functools import prod
from util.more_itertools import flatten


def prepend_digits(digits, number):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (digits, abs(number)))


def append_digits(number, digits):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (abs(number), digits))


def is_palindrome(n):
    digits = str(n)
    reversed_digits = digits[::-1]
    return digits == reversed_digits


def digital_sum(n):
    return sum(map(int, str(n)))


def pythagorean_triples(max_perimeter):
    if max_perimeter < 12:
        return
    q = deque([(2, 1)])
    while q:
        m, n = q.pop()
        # compute the primitive triplet
        if (a := m * m - n * n) > (b := 2 * m * n):
            a, b = b, a
        c = m * m + n * n
        yield a, b, c
        # compute all the multiples of this triplet
        for multiple in range(2, 1 + max_perimeter // (a + b + c)):
            yield a * multiple, b * multiple, c * multiple
        # expand the matrix multiplications and generate the next (m, n) pairs
        for m, n in ((2 * m - n, m), (2 * m + n, m), (m + 2 * n, n)):
            if 2 * (m * (n + m)) <= max_perimeter:
                q.append((m, n))


def prime_factors(number):
    # Source: https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f
    if number < 2:
        return

    for i in itertools.chain((2, 3, 5, 7), range(11, int(number ** .5) + 1, 2)):
        exponent = 0
        while number % i == 0:
            exponent += 1
            number = number / i
        if exponent:
            yield i, exponent

    if number > 2:
        yield int(number), 1


def num_partitions(n):
    partitions = [1] + [0] * n
    for i in range(1, n + 1):
        sign = 1
        for j in range(1, i + 1):
            for k in (i - (j * (3 * j - 1) // 2), i - (-j * (-3 * j - 1) // 2)):
                if k >= 0:
                    partitions[i] += sign * partitions[k]
            sign *= -1
    return partitions[n]


def multiplicative_partitions(n):
    """Yields all (unordered) multiplicative partitions of the integer n.
    A multiplicative partition or unordered factorization of an integer n is a way of writing n as a product of
    integers greater than 1, treating two products as equivalent if they differ only in the ordering of the factors.

    The number 20 has four multiplicative partitions:
        * 2 × 2 × 5
        * 2 × 10
        * 4 × 5
        * 20
    """
    assert n > 0

    def _multiplicative_partitions(_m, _n):
        # Source: Knopfmacher, Arnold & Mays, M.. (2006).
        #   Ordered and Unordered Factorizations of Integers. Mathematica Journal. 10.
        #   Generating Unordered Factorizations
        if _n == 1 or _m == 1:
            yield (),
            return
        divisors = positive_divisors(_n)
        assert next(divisors) == 1  # skip 1 as a divisor
        is_prime = True
        for d in divisors:
            if d != _n:
                is_prime = False
            elif is_prime:
                if _m >= _n:
                    yield _n,
                return
            if d <= _m:
                for partition in _multiplicative_partitions(d, _n // d):
                    yield tuple(flatten((d,) + partition, 1))
            elif not is_prime:
                return

    yield from _multiplicative_partitions(n, n)


def num_divisors(n):
    if n == 0 or n == 1 or n == 2:
        return n
    return prod(((exponent + 1) for _, exponent in prime_factors(n)))


def aliquot_sum(n):
    """The aliquot sum s(n) of a positive integer n is the sum of all proper divisors of n
    (all divisors of n other than n itself).
    """
    if 0 < n < 4:
        return 0
    return prod((base ** (exponent + 1) - 1) // (base - 1) for base, exponent in prime_factors(n)) - n


def positive_divisors(n):
    # positive integers less than or equal to n which divide evenly into n.
    assert n > 0
    return divisors_from_prime_factors(prime_factors(n))


def divisors_from_prime_factors(factors):

    def __generate():
        try:
            prime, exponent = next(factors)
        except StopIteration:
            yield 1
            return
        for factor in __generate():
            prime_to_i = 1
            # prime_to_i iterates prime**i values, i being all possible exponents
            for _ in range(exponent + 1):
                yield factor * prime_to_i
                prime_to_i *= prime

    return __generate()


def factorial(n):
    assert n >= 0
    return prod(range(1, n + 1))


def multiplicative_order(a, m):
    """Computes the multiplicative order of b module n
    i.e., find the small k such that b ** k == 1 mod n
    Source: https://rosettacode.org/wiki/Multiplicative_order#Python
    """
    assert gcd(a, m) == 1

    def _multiplicative_order(_a, _p, _e):
        _m = _p ** _e
        _t = (_p - 1) * (_p ** (_e - 1))
        _qs = [1]
        for factor, exponent in prime_factors(_t):
            _qs = [q * factor ** j for j in range(1 + exponent) for q in _qs]
        _qs.sort()
        for _q in _qs:
            if pow(_a, _q, _m) == 1:
                return _q

    def _lcm(_a, _b):
        return (_a * _b) // gcd(_a, _b)

    return reduce(_lcm, (_multiplicative_order(a, f, e) for f, e in prime_factors(m)))


def simplified_continued_fraction(denominators, base, n):
    if n == 0:
        return base, 1
    numerator = 1
    denominators = list(itertools.islice(denominators, n))
    denominator = denominators[-1]
    for d in denominators[-2::-1]:
        numerator, denominator = denominator, d * denominator + numerator
    return numerator + base * denominator, denominator


def is_square(n):
    return n == isqrt(n) ** 2


def eulers_totient(n):
    """
    Euler's totient function counts the positive integers
    up to a given integer n that are relatively prime to n.
    """
    return prod((
        base ** (exp - 1) * (base - 1)
        for base, exp in prime_factors(n)
    ))


def moebius(n):
    """
    For any positive integer n, define moebius(n) as
    the sum of the primitive nth roots of unity.
    It has values in {−1, 0, 1} depending on the factorization of n into prime factors:

    * moebius(n) = 1 if n is a square-free positive integer with an even number of prime factors.
    * moebius(n) = −1 if n is a square-free positive integer with an odd number of prime factors.
    * moebius(n) = 0 if n has a squared prime factor.
    """
    m = 1
    for base, exp in prime_factors(n):
        if exp >= 2:
            return 0
        m *= -1
    return m


def totient_sum(n):
    phi = list(range(n + 1))
    for i, phi_i in enumerate(phi):
        if i != phi_i or i < 2:
            continue
        for j in range(i, n + 1, i):
            phi[j] -= phi[j] / i
    return sum(phi)


def num_proper_permutations_of_digits(digits, zero_value=0):
    digit_counts = Counter(digits)
    num_zeros = digit_counts.get(zero_value)
    n = len(digits)
    if num_zeros is None:
        return factorial(n) / prod(map(factorial, digit_counts.values()))
    else:
        del digit_counts[zero_value]
        return comb(n - 1, num_zeros) * (factorial(n - num_zeros) / prod(map(factorial, digit_counts.values())))


@total_ordering
class _PositiveInfinity(object):
    def __eq__(self, other):
        return other is POSITIVE_INFINITY

    def __lt__(self, other):
        return False


@total_ordering
class _NegativeInfinity(object):
    def __eq__(self, other):
        return other is NEGATIVE_INFINITY

    def __lt__(self, other):
        return True


POSITIVE_INFINITY = _PositiveInfinity()
NEGATIVE_INFINITY = _NegativeInfinity()
