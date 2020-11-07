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
