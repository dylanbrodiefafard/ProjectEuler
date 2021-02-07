import itertools
from functools import reduce, total_ordering
from math import gcd, isqrt, floor

from util.more_functools import prod


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


def pythagorean_triples(c_max):
    triples = set()
    for a in range(1, c_max + 1):
        b = a + 1
        c = b + 1
        while c <= c_max:
            while c ** 2 < a ** 2 + b ** 2:
                c += 1
            if a ** 2 + b ** 2 == c ** 2 and c <= c_max:
                triples.add((a, b, c))
            b += 1
    return triples


def prime_factors(number):
    # Source: https://paulrohan.medium.com/prime-factorization-of-a-number-in-python-and-why-we-check-upto-the-square-root-of-the-number-111de56541f
    if number < 2:
        return

    exponent = 0
    while number % 2 == 0:
        exponent += 1
        number = number / 2
    if exponent:
        yield 2, exponent

    for i in range(3, int(number ** .5) + 1, 2):
        exponent = 0
        while number % i == 0:
            exponent += 1
            number = number / i
        if exponent:
            yield i, exponent

    if number > 2:
        yield int(number), 1


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
    s = 0
    for k in range(1, n + 1):
        s += moebius(k) * (floor(n / k) ** 2)
    s = (1 + s) / 2
    assert s.is_integer()
    return int(s)


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
