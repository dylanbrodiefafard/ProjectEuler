from itertools import islice

from solutions.BaseSolution import BaseSolution
from util.primes import primes


class Solution7(BaseSolution):
    NUMBER = 7
    VERIFIED_ANSWER = 104743

    def run_tests(self, test_case):
        test_case.assertEqual(13, self.get_nth_prime(6))

    @staticmethod
    def get_nth_prime(n):
        return next(islice(primes(), n - 1, None))

    def get_answer(self):
        return self.get_nth_prime(10001)


if __name__ == '__main__':
    Solution7().print_answer()
