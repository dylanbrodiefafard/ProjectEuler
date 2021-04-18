from unittest import TestCase

from util.more_itertools import *


class MoreItertoolsTest(TestCase):
    def test_exactly_n(self):
        self.assertTrue(exactly_n([], 0))
        self.assertTrue(exactly_n([1], 1))
        self.assertTrue(exactly_n([1, 2], 2))
        self.assertFalse(exactly_n([1, 2], 1))
        self.assertFalse(exactly_n([1], 0))
        self.assertFalse(exactly_n([1, 2, 3], 2))

    def test_first_true(self):
        self.assertFalse(first_true(()))
        self.assertEqual(2, first_true((False, [], 2, 3)))
        self.assertEqual(3, first_true((False, [], {}), default=3))
        self.assertEqual(4, first_true((2, 3, 4, 5), default=3, predicate=lambda x: x > 3))
        self.assertEqual(42, first_true((2, 3, -4, -5), default=42, predicate=lambda x: x > 3))

    def test_str_product(self):
        self.assertListEqual(['A1', 'A2', 'A3'], list(str_product('A', '123')))
        self.assertListEqual(['1A', '2A', '3A'], list(str_product('123', 'A')))
        self.assertListEqual(['16', '16', '26', '26', '36', '36'], list(str_product('123', '66')))

    def test_flatten(self):
        numbers = (0, (1, 2), [3, 4], (5, (((6,),), )))
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6], list(flatten(numbers)))
        self.assertListEqual([0, 1, 2, 3, 4, 5, (((6,),),)], list(flatten(numbers, 1)))
        self.assertListEqual([0, 1, 2, 3, 4, 5, ((6,),)], list(flatten(numbers, 2)))
        self.assertListEqual([0, 1, 2, 3, 4, 5, (6,)], list(flatten(numbers, 3)))
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6], list(flatten(numbers, 4)))
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6], list(flatten(numbers, 5)))

    def test_nth(self):
        self.assertEqual(1, nth([1], 0))
        self.assertIsNone(nth([1], 1))
        self.assertEqual(0, nth([1], 1, default=0))
        self.assertEqual(2, nth([1, 2], 1, default=0))
        self.assertEqual(99, nth(range(100), 99))
