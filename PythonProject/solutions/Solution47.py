from solutions.SolutionBase import SolutionBase
from util.integers import prime_factors
from util.more_itertools import exactly_n
from util.sequences import positive_integers


class Solution47(SolutionBase):
    NUMBER = 47
    VERIFIED_ANSWER = 134043

    def run_tests(self, test_case):
        test_case.assertEqual((14, 15), self.first_n_consecutive_numbers_with_n_prime_factors(2))
        test_case.assertEqual((644, 645, 646), self.first_n_consecutive_numbers_with_n_prime_factors(3))

    @staticmethod
    def first_n_consecutive_numbers_with_n_prime_factors(n: int):
        num_consecutive = 0
        for m in positive_integers():
            if exactly_n(prime_factors(m), n):
                num_consecutive += 1
                if num_consecutive == n:
                    return tuple(m - (n - i - 1) for i in range(n))
            else:
                num_consecutive = 0

    def get_answer(self):
        return self.first_n_consecutive_numbers_with_n_prime_factors(4)[0]


if __name__ == '__main__':
    Solution47().print_answer()
