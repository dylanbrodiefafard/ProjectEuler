from collections import defaultdict

from solutions.SolutionBase import SolutionBase
from util.integers import pythagorean_triples


class Solution75(SolutionBase):
    NUMBER = 75
    VERIFIED_ANSWER = 161667

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        num_solutions_by_perimeter = defaultdict(int)
        for a, b, c in pythagorean_triples(1500000):
            num_solutions_by_perimeter[a + b + c] += 1
        num_values = 0
        for num_solutions in num_solutions_by_perimeter.values():
            if num_solutions == 1:
                num_values += 1
        return num_values


if __name__ == '__main__':
    Solution75().print_answer()
