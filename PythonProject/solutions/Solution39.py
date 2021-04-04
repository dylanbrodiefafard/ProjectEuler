from collections import defaultdict

from solutions.SolutionBase import SolutionBase
from util.integers import pythagorean_triples


class Solution39(SolutionBase):
    NUMBER = 39
    VERIFIED_ANSWER = 840

    def run_tests(self, test_case):
        triples = pythagorean_triples(120)
        solutions = set()
        for a, b, c in triples:
            if a + b + c == 120:
                solutions.add((a, b, c))
        test_case.assertSetEqual(solutions, {(20, 48, 52), (24, 45, 51), (30, 40, 50)})

    def get_answer(self):
        num_triples_by_perimeter = defaultdict(int)
        for a, b, c in pythagorean_triples(1000):
            num_triples_by_perimeter[a + b + c] += 1
        return sorted(num_triples_by_perimeter.items(), key=lambda i: i[1])[-1][0]


if __name__ == '__main__':
    Solution39().print_answer()
