from unittest import TestCase

from util.integers import *


class IntegersTest(TestCase):

    def test_prepend_digit(self):
        self.assertEqual(21, prepend_digits(2, 1))
        self.assertEqual(211, prepend_digits(2, 11))
        self.assertEqual(11, prepend_digits(0, 11))
        self.assertEqual(10, prepend_digits(1, 0))
        self.assertEqual(-11, prepend_digits(1, -1))
        self.assertEqual(-1100, prepend_digits(1, -100))
        self.assertEqual(909123, prepend_digits(90, 9123))
        self.assertEqual(123456, prepend_digits(123, 456))
        self.assertEqual(-123456, prepend_digits(123, -456))

    def test_append_digit(self):
        self.assertEqual(21, append_digits(2, 1))
        self.assertEqual(211, append_digits(2, 11))
        self.assertEqual(11, append_digits(0, 11))
        self.assertEqual(10, append_digits(1, 0))
        self.assertEqual(-11, append_digits(-1, 1))
        self.assertEqual(-1100, append_digits(-1, 100))
        self.assertEqual(909123, append_digits(90, 9123))
        self.assertEqual(123456, append_digits(123, 456))
        self.assertEqual(-123456, append_digits(-123, 456))

    def test_is_paldindrome(self):
        self.assertTrue(is_palindrome(313))
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(11))
        self.assertTrue(is_palindrome(3))
        self.assertTrue(is_palindrome(1000009000001))
        self.assertFalse(is_palindrome(1000009100001))
        self.assertFalse(is_palindrome(13))
        self.assertFalse(is_palindrome(1011))
        self.assertFalse(is_palindrome(9000091))

    def test_digital_sum(self):
        self.assertEqual(1, digital_sum(1))
        self.assertEqual(2, digital_sum(11))
        self.assertEqual(1, digital_sum(100))
        self.assertEqual(15, digital_sum(12345))
        self.assertEqual(15, digital_sum(123450))
        self.assertEqual(15, digital_sum(123405))
        self.assertEqual(15, digital_sum(102345))

    def test_pythagorean_triples(self):
        self.assertSetEqual({(3, 4, 5)}, pythagorean_triples(5))
        self.assertSetEqual({(3, 4, 5), (6, 8, 10), (5, 12, 13)}, pythagorean_triples(13))
        self.assertSetEqual({(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (7, 24, 25),
                             (15, 20, 25), (10, 24, 26), (20, 21, 29), (18, 24, 30)}, pythagorean_triples(30))

    def test_prime_factors(self):
        self.assertListEqual([], list(prime_factors(0)))
        self.assertListEqual([], list(prime_factors(1)))
        self.assertListEqual([2], list(prime_factors(2)))
        self.assertListEqual([3], list(prime_factors(3)))
        self.assertListEqual([2, 2, 3], list(prime_factors(12)))
        self.assertListEqual([3, 7, 7], list(prime_factors(147)))
        self.assertListEqual([2, 3, 5, 11], list(prime_factors(330)))

    def test_num_divisors(self):
        self.assertEqual(0, num_divisors(0))
        self.assertEqual(1, num_divisors(1))
        self.assertEqual(2, num_divisors(2))
        self.assertEqual(2, num_divisors(3))
        self.assertEqual(6, num_divisors(12))
        self.assertEqual(8, num_divisors(30))
        self.assertEqual(10, num_divisors(48))
        self.assertEqual(3, num_divisors(49))

    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))
        self.assertEqual(6, factorial(3))
        self.assertEqual(1307674368000, factorial(15))
        self.assertEqual(2432902008176640000, factorial(20))
