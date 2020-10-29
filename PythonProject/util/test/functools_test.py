from unittest import TestCase

from util.functools import *


class FunctoolsTest(TestCase):
    def test_prod(self):
        self.assertEqual(1, prod([]))
        self.assertEqual(1, prod([1]))
        self.assertEqual(1, prod([1, 1]))
        self.assertEqual(0, prod([1, 0]))
        self.assertEqual(0, prod([0, 1]))
        self.assertEqual(2, prod([1, 2]))
        self.assertEqual(-2, prod([1, -2]))
        self.assertEqual(2, prod([-1, -2]))
        self.assertEqual(2432902008176640000, prod(range(1, 20 + 1)))
