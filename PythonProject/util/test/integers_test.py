from decimal import Decimal
from itertools import cycle, islice, chain
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

    def test_is_palindrome(self):
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
        self.assertSetEqual({(3, 4, 5)}, set(pythagorean_triples(12)))
        self.assertSetEqual({(3, 4, 5), (6, 8, 10), (5, 12, 13)}, set(pythagorean_triples(30)))
        self.assertSetEqual({(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (7, 24, 25),
                             (15, 20, 25), (10, 24, 26), (20, 21, 29), (18, 24, 30)}, set(pythagorean_triples(73)))

    def test_prime_factors(self):
        self.assertListEqual([], list(prime_factors(0)))
        self.assertListEqual([], list(prime_factors(1)))
        self.assertListEqual([(2, 1)], list(prime_factors(2)))
        self.assertListEqual([(3, 1)], list(prime_factors(3)))
        self.assertListEqual([(2, 2), (3, 1)], list(prime_factors(12)))
        self.assertListEqual([(3, 1), (7, 2)], list(prime_factors(147)))
        self.assertListEqual([(2, 1), (3, 1), (5, 1), (11, 1)], list(prime_factors(330)))

    def test_num_partitions(self):
        self.assertEqual(1, num_partitions(1))
        self.assertEqual(2, num_partitions(2))
        self.assertEqual(3, num_partitions(3))
        self.assertEqual(5, num_partitions(4))
        self.assertEqual(7, num_partitions(5))
        self.assertEqual(173525, num_partitions(49))

    def test_multiplicative_partitions(self):
        partitions = sorted(multiplicative_partitions(24))
        self.assertTupleEqual((3, 2, 2, 2), partitions[0])
        self.assertTupleEqual((4, 3, 2), partitions[1])
        self.assertTupleEqual((6, 2, 2), partitions[2])
        self.assertTupleEqual((6, 4), partitions[3])
        self.assertTupleEqual((8, 3), partitions[4])
        self.assertTupleEqual((12, 2), partitions[5])
        self.assertTupleEqual((24,), partitions[6])
        self.assertEqual(7, len(partitions))
        partitions = sorted(multiplicative_partitions(81))
        self.assertTupleEqual((3, 3, 3, 3), partitions[0])
        self.assertTupleEqual((9, 3, 3), partitions[1])
        self.assertTupleEqual((9, 9), partitions[2])
        self.assertTupleEqual((27, 3), partitions[3])
        self.assertTupleEqual((81,), partitions[4])
        self.assertEqual(5, len(partitions))
        partitions = sorted(multiplicative_partitions(3343))
        self.assertTupleEqual((3343,), partitions[0])
        self.assertEqual(1, len(partitions))

    def test_positive_divisors(self):
        self.assertListEqual([1], sorted(positive_divisors(1)))
        self.assertListEqual([1, 2], sorted(positive_divisors(2)))
        self.assertListEqual([1, 3], sorted(positive_divisors(3)))
        self.assertListEqual([1, 2, 3, 4, 6, 12], sorted(positive_divisors(12)))
        self.assertListEqual([1, 3, 7, 21, 49, 147], sorted(positive_divisors(147)))
        self.assertListEqual([1, 2, 3, 5, 6, 10, 11, 15, 22, 30, 33, 55, 66, 110, 165, 330], sorted(positive_divisors(330)))

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

    def test_multiplicative_order(self):
        self.assertEqual(1, multiplicative_order(1, 2))
        self.assertEqual(3, multiplicative_order(4, 9))
        self.assertEqual(6, multiplicative_order(14, 9))
        self.assertEqual(6, multiplicative_order(140, 9))
        self.assertEqual(3, multiplicative_order(1024, 9))
        self.assertEqual(1, multiplicative_order(666, 19))

    def test_aliquot_sum(self):
        self.assertEqual(9, aliquot_sum(15))
        self.assertEqual(15, aliquot_sum(16))
        self.assertEqual(1, aliquot_sum(17))
        self.assertEqual(42, aliquot_sum(30))
        self.assertEqual(106, aliquot_sum(80))

    def test_is_square(self):
        self.assertTrue(is_square(16))
        self.assertTrue(is_square(4))
        self.assertTrue(is_square(9))
        self.assertTrue(is_square(152415789666209426002111556165263283035677489))
        self.assertFalse(is_square(10))
        self.assertFalse(is_square(17))
        self.assertFalse(is_square(48))
        self.assertFalse(is_square(152415789666209426002111556165263283035677490))

    def test_eulers_totient(self):
        self.assertEqual(1, eulers_totient(1))
        self.assertEqual(1, eulers_totient(2))
        self.assertEqual(2, eulers_totient(3))
        self.assertEqual(2, eulers_totient(4))
        self.assertEqual(4, eulers_totient(12))
        self.assertEqual(8, eulers_totient(30))
        self.assertEqual(144, eulers_totient(468))
        self.assertEqual(396, eulers_totient(469))

    def test_mobius(self):
        self.assertEqual(-1, moebius(2))
        self.assertEqual(-1, moebius(3))
        self.assertEqual(-1, moebius(5))
        self.assertEqual(-1, moebius(30))
        self.assertEqual(0, moebius(4))
        self.assertEqual(0, moebius(8))
        self.assertEqual(0, moebius(9))
        self.assertEqual(0, moebius(27))
        self.assertEqual(1, moebius(1))
        self.assertEqual(1, moebius(6))
        self.assertEqual(1, moebius(10))
        self.assertEqual(1, moebius(22))

    def test_totient_sum(self):
        self.assertEqual(1, totient_sum(1))
        self.assertEqual(2, totient_sum(2))
        self.assertEqual(4, totient_sum(3))
        self.assertEqual(360, totient_sum(34))
        self.assertEqual(964, totient_sum(56))

    def test_num_proper_permutations_of_digits(self):
        self.assertEqual(1, num_proper_permutations_of_digits([1]))
        self.assertEqual(2, num_proper_permutations_of_digits([1, 2]))
        self.assertEqual(4, num_proper_permutations_of_digits([1, 2, 0]))
        self.assertEqual(1, num_proper_permutations_of_digits([0, 1]))
        self.assertEqual(1, num_proper_permutations_of_digits([1, 1]))
        self.assertEqual(1050, num_proper_permutations_of_digits([0, 0, 0, 1, 1, 3, 7, 7]))
        self.assertEqual(1050, num_proper_permutations_of_digits(['0', '0', '0', '1', '1', '3', '7', '7'], zero_value='0'))

    def test_sqrt_continued_fraction(self):
        def get_terms(n):
            return tuple(islice(sqrt_continued_fraction(n), 12))
        self.assertTupleEqual((1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2), get_terms(2))
        self.assertTupleEqual((1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1), get_terms(3))
        self.assertTupleEqual((2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4), get_terms(5))
        self.assertTupleEqual((2, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1), get_terms(7))
        self.assertTupleEqual((3, 1, 1, 1, 1, 6, 1, 1, 1, 1, 6, 1), get_terms(13))
        self.assertTupleEqual((4, 2, 1, 3, 1, 2, 8, 2, 1, 3, 1, 2), get_terms(19))
        self.assertTupleEqual((5, 1, 1, 3, 5, 3, 1, 1, 10, 1, 1, 3), get_terms(31))
        self.assertTupleEqual((6, 1, 1, 3, 1, 5, 1, 3, 1, 1, 12, 1), get_terms(43))
        self.assertTupleEqual((7, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14), get_terms(50))
        self.assertTupleEqual((7, 1, 4, 3, 1, 2, 2, 1, 3, 4, 1, 14), get_terms(61))
        self.assertTupleEqual((8, 5, 2, 1, 1, 7, 1, 1, 2, 5, 16, 5), get_terms(67))
        self.assertTupleEqual((8, 1, 2, 1, 1, 5, 4, 5, 1, 1, 2, 1), get_terms(76))
        self.assertTupleEqual((9, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18), get_terms(82))
        self.assertTupleEqual((9, 1, 2, 3, 1, 1, 5, 1, 8, 1, 5, 1), get_terms(94))
        self.assertTupleEqual((9, 1, 18, 1, 18, 1, 18, 1, 18, 1, 18, 1), get_terms(99))

    def test_continued_fraction_convergents(self):
        def get_convergents(first_term, repeating_terms, n):
            return tuple(islice(continued_fraction_convergents(chain([first_term], cycle(repeating_terms))), n))

        self.assertTupleEqual(
            ((1, 1), (3, 2), (7, 5), (17, 12), (41, 29), (99, 70), (239, 169), (577, 408)),
            get_convergents(1, [2], 8)  # sqrt 2
        )
        self.assertTupleEqual(
            ((1, 1), (2, 1), (5, 3), (7, 4), (19, 11), (26, 15), (71, 41), (97, 56)),
            get_convergents(1, [1, 2], 8)  # sqrt 3
        )
        self.assertTupleEqual(
            ((2, 1), (9, 4), (38, 17), (161, 72)),
            get_convergents(2, [4], 4)  # sqrt 5
        )
        self.assertTupleEqual(
            ((0, 1), (1, 1), (5, 6), (11, 13), (27, 32)),
            get_convergents(0, [1, 5, 2, 2], 5)  # Test with continued fraction for 0.84375: [0;1,5,2,2]
        )
        self.assertTupleEqual(
            ((3, 1), (22, 7), (333, 106), (355, 113)),
            get_convergents(3, [7, 15, 1], 4)  # Test with pi
        )
