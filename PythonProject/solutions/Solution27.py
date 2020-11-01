from collections import namedtuple

from solutions.SolutionBase import SolutionBase
from util.primes import is_prime, primes_up_to


class Solution27(SolutionBase):
    NUMBER = 27
    VERIFIED_ANSWER = -59231

    def run_tests(self, test_case):
        test_case.assertEqual((-1, 41), self.coefficients_for_quadratic_with_max_consecutive_primes(41))

    @staticmethod
    def num_consecutive_primes(a: int, b: int):
        n = 0
        while True:
            if not is_prime(n ** 2 + a * n + b):
                break
            n += 1
        return n

    @staticmethod
    def coefficients_for_quadratic_with_max_consecutive_primes(max_b: int):
        assert max_b != 0
        Answer = namedtuple('Answer', ['num_consecutive_primes', 'coefficients'])
        prime_list = list(primes_up_to(max_b))
        answer = Answer(-1, (None, None))
        for a in range(-max_b, max_b + 1):
            for b in prime_list:
                n = Solution27.num_consecutive_primes(a, b)
                if n > answer.num_consecutive_primes:
                    answer = Answer(n, (a, b))
        return answer.coefficients

    def get_answer(self):
        a, b = self.coefficients_for_quadratic_with_max_consecutive_primes(1000)
        return a * b


if __name__ == '__main__':
    Solution27().print_answer()
