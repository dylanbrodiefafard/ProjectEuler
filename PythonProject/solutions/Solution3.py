from solutions.BaseSolution import BaseSolution
from util.integers import prime_factors


class Solution3(BaseSolution):
    NUMBER = 3
    VERIFIED_ANSWER = 6857

    def run_tests(self, test_case):
        test_case.assertEqual(29, self.get_largest_prime_factor(13195))

    @staticmethod
    def get_largest_prime_factor(n):
        return max((factor for factor, _ in prime_factors(n)))

    def get_answer(self):
        return self.get_largest_prime_factor(600851475143)


if __name__ == '__main__':
    Solution3().print_answer()
