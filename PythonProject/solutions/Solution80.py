from decimal import Decimal, getcontext

from solutions.SolutionBase import SolutionBase
from util.integers import is_square


class Solution80(SolutionBase):
    NUMBER = 80
    VERIFIED_ANSWER = 40886

    def run_tests(self, test_case):
        test_case.assertEqual(475, self.digital_sum_of_first_n_decimal_digits_of_sqrt(2, 100))

    @staticmethod
    def digital_sum_of_first_n_decimal_digits_of_sqrt(m, n):
        getcontext().prec = n + 2
        digits = str(Decimal(m).sqrt()).replace('.', '')
        return sum(map(int, digits[:n]))

    def get_answer(self):
        total = 0
        for n in range(100):
            if not is_square(n):
                total += self.digital_sum_of_first_n_decimal_digits_of_sqrt(n, 100)
        return total


if __name__ == '__main__':
    Solution80().print_answer()
