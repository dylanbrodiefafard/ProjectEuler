from collections import Counter

from solutions.BaseSolution import BaseSolution
from util.functools import prod
from util.integers import prime_factors


class Solution5(BaseSolution):
    NUMBER = 5
    VERIFIED_ANSWER = 232792560

    def run_tests(self, test_case):
        test_case.assertEqual(2520, self.smallest_number_evenly_divisible_by_all(10))

    @staticmethod
    def smallest_number_evenly_divisible_by_all(max_val):
        assert max_val > 0
        if max_val == 1:
            return 1
        if max_val == 2:
            return 2
        max_power_of_prime_factors = {}
        for n in range(2, max_val + 1):
            for factor, count in Counter(prime_factors(n)).items():
                max_power_of_prime_factors[factor] = max(max_power_of_prime_factors.get(factor, 0), count)
        return prod((factor ** power for factor, power in max_power_of_prime_factors.items()))

    def get_answer(self):
        return self.smallest_number_evenly_divisible_by_all(20)


if __name__ == '__main__':
    Solution5().print_answer()
