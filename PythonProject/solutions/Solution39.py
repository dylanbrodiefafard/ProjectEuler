from collections import defaultdict
from math import sqrt, ceil

from solutions.SolutionBase import SolutionBase


class Solution39(SolutionBase):
    NUMBER = 39
    VERIFIED_ANSWER = 840

    def run_tests(self, test_case):
        triples = self.get_pythagorean_triples(120)
        solutions = set()
        for a, b, c in triples:
            if a + b + c == 120:
                solutions.add((a, b, c))
        test_case.assertSetEqual(solutions, {(20, 48, 52), (24, 45, 51), (30, 40, 50)})

    @staticmethod
    def get_pythagorean_triples(c_max):
        pythagorean_triples = set()
        a_max = int(ceil(sqrt(c_max / 2))) + int(ceil(c_max / 2))
        for a in range(1, a_max):
            for b in range(a, a_max):
                c = sqrt(a ** 2 + b ** 2)
                if c != int(c):
                    continue
                pythagorean_triples.add((a, b, int(c)))
        return pythagorean_triples

    def get_answer(self):
        num_triples_by_perimeter = defaultdict(int)
        for a, b, c in self.get_pythagorean_triples(1000):
            num_triples_by_perimeter[a + b + c] += 1
        return sorted(num_triples_by_perimeter.items(), key=lambda i: i[1])[-1][0]


if __name__ == '__main__':
    Solution39().print_answer()
