from itertools import islice
from unittest import TestCase

from util.sequences import *


class SequencesTest(TestCase):
    def test_positive_integers(self):
        integers_gen = positive_integers()
        self.assertListEqual([1, 2, 3, 4, 5], list(islice(integers_gen, 5)))
        list(islice(integers_gen, 20))
        self.assertListEqual([26, 27, 28, 29, 30], list(islice(integers_gen, 5)))

    def test_triangular_numbers(self):
        triangle_gen = triangular_numbers()
        self.assertListEqual([0, 1, 3, 6, 10], list(islice(triangle_gen, 5)))
        list(islice(triangle_gen, 20))
        self.assertListEqual([325, 351, 378, 406, 435], list(islice(triangle_gen, 5)))
        self.assertListEqual([6, 10, 15, 21, 28], list(islice(triangular_numbers(3), 5)))

    def test_squares(self):
        square_gen = squares()
        self.assertListEqual([0, 1, 4, 9, 16], list(islice(square_gen, 5)))
        list(islice(square_gen, 20))
        self.assertListEqual([625, 676, 729, 784, 841], list(islice(square_gen, 5)))

    def test_pentagonal_numbers(self):
        pentagonal_gen = pentagonal_numbers()
        self.assertListEqual([0, 1, 5, 12, 22], list(islice(pentagonal_gen, 5)))
        list(islice(pentagonal_gen, 20))
        self.assertListEqual([925, 1001, 1080, 1162, 1247], list(islice(pentagonal_gen, 5)))

    def test_hexagonal_numbers(self):
        hexagonal_gen = hexagonal_numbers()
        self.assertListEqual([0, 1, 6, 15, 28], list(islice(hexagonal_gen, 5)))
        list(islice(hexagonal_gen, 20))
        self.assertListEqual([1225, 1326, 1431, 1540, 1653], list(islice(hexagonal_gen, 5)))

    def test_heptagonal_numbers(self):
        heptagonal_gen = heptagonal_numbers()
        self.assertListEqual([0, 1, 7, 18, 34], list(islice(heptagonal_gen, 5)))
        list(islice(heptagonal_gen, 20))
        self.assertListEqual([1525, 1651, 1782, 1918, 2059], list(islice(heptagonal_gen, 5)))

    def test_octagonal_numbers(self):
        octagonal_gen = octagonal_numbers()
        self.assertListEqual([0, 1, 8, 21, 40], list(islice(octagonal_gen, 5)))
        list(islice(octagonal_gen, 20))
        self.assertListEqual([1825, 1976, 2133, 2296, 2465], list(islice(octagonal_gen, 5)))

    def test_ulams_spiral_diagonal_numbers(self):
        self.assertListEqual(
            [1, 3, 5, 7, 9],
            list(islice(ulams_spiral_diagonal_numbers(), 5))
        )
        self.assertListEqual(
            [1, 3, 5, 7, 9, 13, 17, 21, 25],
            list(islice(ulams_spiral_diagonal_numbers(), 9))
        )
        self.assertListEqual(
            [1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49],
            list(islice(ulams_spiral_diagonal_numbers(), 13))
        )

    def test_abundant_numbers(self):
        abundant_gen = abundant_numbers()
        self.assertListEqual([12, 18, 20, 24, 30], list(islice(abundant_gen, 5)))
        list(islice(abundant_gen, 20))
        self.assertListEqual([112, 114, 120, 126, 132], list(islice(abundant_gen, 5)))

    def test_prime_numbers(self):
        primes_gen = prime_numbers()
        # test primes 1-5 are correct
        self.assertListEqual([2, 3, 5, 7, 11], list(islice(primes_gen, 5)))
        list(islice(primes_gen, 95))  # skip 95 primes
        # test that primes 101-105 are correct
        self.assertListEqual([547, 557, 563, 569, 571], list(islice(primes_gen, 5)))

    def test_prime_numbers_up_to(self):
        primes_gen = prime_numbers_up_to(571)
        # test primes 1-5 are correct
        self.assertListEqual([2, 3, 5, 7, 11], list(islice(primes_gen, 5)))
        list(islice(primes_gen, 95))  # skip 95 primes
        # test that primes 101-105 are correct
        self.assertListEqual([547, 557, 563, 569, 571], list(islice(primes_gen, 5)))
