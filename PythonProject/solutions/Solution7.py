from itertools import islice

from solutions.SolutionBase import SolutionBase
from util.sequences import prime_numbers


class Solution7(SolutionBase):
    NUMBER = 7
    VERIFIED_ANSWER = 104743

    def run_tests(self, test_case):
        test_case.assertEqual(13, self.get_nth_prime(6))

    @staticmethod
    def get_nth_prime(n):
        return next(islice(prime_numbers(), n - 1, None))

    def get_answer(self):
        return self.get_nth_prime(10001)


if __name__ == '__main__':
    Solution7().print_answer()
