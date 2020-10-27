def prepend_digits(digits, number):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (digits, abs(number)))


def append_digits(number, digits):
    sign = 1 if number >= 0 else -1
    return sign * int('%d%d' % (abs(number), digits))


def is_paldindrome(n):
    digits = str(n)
    reversed_digits = digits[::-1]
    return digits == reversed_digits


def digital_sum(n):
    return sum(map(int, str(n)))
