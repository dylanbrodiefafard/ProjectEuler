from itertools import islice
from unittest import TestCase

from util.sequences import *


class SequencesTest(TestCase):
    def test_triangular(self):
        triangular_gen = triangular()
        self.assertListEqual([0, 1, 3, 6, 10], list(islice(triangular_gen, 5)))
        list(islice(triangular_gen, 20))
        self.assertListEqual([325, 351, 378, 406, 435], list(islice(triangular_gen, 5)))

    def test_pentagonal(self):
        pentagonal_gen = pentagonal()
        self.assertListEqual([0, 1, 5, 12, 22], list(islice(pentagonal_gen, 5)))
        list(islice(pentagonal_gen, 20))
        self.assertListEqual([925, 1001, 1080, 1162, 1247], list(islice(pentagonal_gen, 5)))

    def test_hexagonal(self):
        hexagonal_gen = hexagonal()
        self.assertListEqual([0, 1, 6, 15, 28], list(islice(hexagonal_gen, 5)))
        list(islice(hexagonal_gen, 20))
        self.assertListEqual([1225, 1326, 1431, 1540, 1653], list(islice(hexagonal_gen, 5)))
