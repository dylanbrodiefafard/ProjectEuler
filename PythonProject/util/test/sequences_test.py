from itertools import islice
from unittest import TestCase

from util.sequences import *


class SequencesTest(TestCase):
    def test_triangle(self):
        triangle_gen = triangle()
        self.assertListEqual([0, 1, 3, 6, 10], list(islice(triangle_gen, 5)))
        list(islice(triangle_gen, 20))
        self.assertListEqual([325, 351, 378, 406, 435], list(islice(triangle_gen, 5)))

    def test_square(self):
        square_gen = square()
        self.assertListEqual([0, 1, 4, 9, 16], list(islice(square_gen, 5)))
        list(islice(square_gen, 20))
        self.assertListEqual([625, 676, 729, 784, 841], list(islice(square_gen, 5)))

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

    def test_heptagonal(self):
        heptagonal_gen = heptagonal()
        self.assertListEqual([0, 1, 7, 18, 34], list(islice(heptagonal_gen, 5)))
        list(islice(heptagonal_gen, 20))
        self.assertListEqual([1525, 1651, 1782, 1918, 2059], list(islice(heptagonal_gen, 5)))

    def test_octagonal(self):
        octagonal_gen = octagonal()
        self.assertListEqual([0, 1, 8, 21, 40], list(islice(octagonal_gen, 5)))
        list(islice(octagonal_gen, 20))
        self.assertListEqual([1825, 1976, 2133, 2296, 2465], list(islice(octagonal_gen, 5)))

    def test_spiral_diagonal(self):
        self.assertListEqual(
            [3, 5, 7, 9],
            list(islice(spiral_diagonal(), 4))
        )
        self.assertListEqual(
            [3, 5, 7, 9, 13, 17, 21, 25],
            list(islice(spiral_diagonal(), 8))
        )
        self.assertListEqual(
            [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49],
            list(islice(spiral_diagonal(), 12))
        )
