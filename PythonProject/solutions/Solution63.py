from math import ceil

from solutions.SolutionBase import SolutionBase
from util.sequences import positive_integers


class Solution63(SolutionBase):
    NUMBER = 63
    VERIFIED_ANSWER = 49

    def run_tests(self, test_case):
        test_case.assertListEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], list(self.n_digit_nth_power_positive_integers(1)))
        test_case.assertListEqual([16, 25, 36, 49, 64, 81], list(self.n_digit_nth_power_positive_integers(2)))

    @staticmethod
    def n_digit_nth_power_positive_integers(n):
        min_val, max_val = 10 ** (n - 1), 10 ** n - 1
        m = int(ceil(min_val ** (1 / n)))
        while True:
            nth_power = m ** n
            if nth_power > max_val:
                return
            yield nth_power
            m += 1

    def get_answer(self):
        count = 0
        for n in positive_integers():
            count += (n_count := len(list(self.n_digit_nth_power_positive_integers(n))))
            if n_count == 0:
                # This must mean that the power is now too high to generate any n-digit numbers.
                # Going to a higher power won't change that now.
                return count


if __name__ == '__main__':
    Solution63().print_answer()
