from util.functools import prod


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

    while number % 2 == 0:
        yield 2
        number = number / 2

    for i in range(3, int(number ** .5) + 1, 2):
        while number % i == 0:
            yield i
            number = number / i

    if number > 2:
        yield int(number)


def num_divisors(n):
    if n == 0 or n == 1 or n == 2:
        return n
    num = 1
    prime_factors_gen = prime_factors(n)
    last_prime_factor = next(prime_factors_gen)
    power_of_last_prime_factor = 1
    for prime_factor in prime_factors_gen:
        if last_prime_factor == prime_factor:
            power_of_last_prime_factor += 1
        else:
            num *= (power_of_last_prime_factor + 1)
            power_of_last_prime_factor = 1
        last_prime_factor = prime_factor
    return num * (power_of_last_prime_factor + 1)


def factorial(n):
    assert n >= 0
    return prod(range(1, n + 1))
