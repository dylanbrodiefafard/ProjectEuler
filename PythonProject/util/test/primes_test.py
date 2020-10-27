from itertools import islice
from unittest import TestCase

from util.primes import *


class PrimesTest(TestCase):
    def test_primes(self):
        primes_gen = primes()
        # test primes 1-5 are correct
        self.assertListEqual([2, 3, 5, 7, 11], list(islice(primes_gen, 5)))
        list(islice(primes_gen, 95))  # skip 95 primes
        # test that primes 101-105 are correct
        self.assertListEqual([547, 557, 563, 569, 571], list(islice(primes_gen, 5)))

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(7789))
        self.assertFalse(is_prime(7791))
        self.assertTrue(is_prime(982451653))
