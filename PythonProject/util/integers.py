import itertools
from functools import reduce
from math import gcd

from util.more_functools import prod


def prepend_digits(digits: int, number: int):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (digits, abs(number)))


def append_digits(number: int, digits: int):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (abs(number), digits))


def is_palindrome(n: int):
    digits = str(n)
    reversed_digits = digits[::-1]
    return digits == reversed_digits


def digital_sum(n: int):
    return sum(map(int, str(n)))


def pythagorean_triples(c_max: int):
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


def prime_factors(number: int):
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


def num_divisors(n: int):
    if n == 0 or n == 1 or n == 2:
        return n
    return prod(((exponent + 1) for _, exponent in prime_factors(n)))


def proper_factors(n: int):
    # numbers less than n which divide evenly into n
    assert n > 0
    all_factors = {1}
    prime_counts = {factor: exponent for factor, exponent in prime_factors(n)}
    all_factors.update(prime_counts.keys())
    exponents = itertools.product(*(range(n + 1) for n in prime_counts.values()))
    factors = (zip(prime_counts.keys(), e) for e in exponents if sum(e) >= 2)
    all_factors.update((prod(p ** e for p, e in f) for f in factors))
    all_factors.remove(n)
    return sorted(all_factors)


def factorial(n: int):
    assert n >= 0
    return prod(range(1, n + 1))


def multiplicative_order(a: int, m: int):
    # Computes the multiplicative order of b module n
    # i.e., find the small k such that b ** k == 1 mod n
    # Source: https://rosettacode.org/wiki/Multiplicative_order#Python
    assert gcd(a, m) == 1

    def _mult_ord(_a, _p, _e):
        _m = _p ** _e
        _t = (_p - 1) * (_p ** (_e - 1))
        _qs = [1]
        for factor, exponent in prime_factors(_t):
            _qs = [q * factor ** j for j in range(1 + exponent) for q in _qs]
        _qs.sort()
        for _q in _qs:
            if pow(_a, _q, _m) == 1:
                return _q

    def lcm(_a, _b):
        return (_a * _b) / gcd(_a, _b)

    return reduce(lcm, (_mult_ord(a, f, e) for f, e in prime_factors(m)))
