from itertools import islice

from solutions.SolutionBase import SolutionBase
from util.sequences import ulams_spiral_diagonal_numbers


class Solution28(SolutionBase):
    NUMBER = 28
    VERIFIED_ANSWER = 669171001

    def run_tests(self, test_case):
        test_case.assertEqual(101, self.sum_of_diagonal_on_spiral(5))

    @staticmethod
    def sum_of_diagonal_on_spiral(n: int):
        assert n > 0
        num_layers = (n - 1) // 2
        return sum(islice(ulams_spiral_diagonal_numbers(), 1 + 4 * num_layers))

    def get_answer(self):
        return self.sum_of_diagonal_on_spiral(1001)


if __name__ == '__main__':
    Solution28().print_answer()
