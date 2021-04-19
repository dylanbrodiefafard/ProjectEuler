from solutions.SolutionBase import SolutionBase
from util.integers import is_square, sqrt_continued_fraction_finite


class Solution64(SolutionBase):
    NUMBER = 64
    VERIFIED_ANSWER = 1322

    def run_tests(self, test_case):
        test_case.assertEqual(4, self.num_sqrt_continued_fractions_with_odd_period(13))

    @staticmethod
    def num_sqrt_continued_fractions_with_odd_period(max_n):
        num_with_odd_period = 0
        for n in range(2, max_n + 1):
            if is_square(n):
                continue
            continued_fraction = sqrt_continued_fraction_finite(n)
            if len(continued_fraction[1:]) % 2 != 0:
                num_with_odd_period += 1
        return num_with_odd_period

    def get_answer(self):
        return self.num_sqrt_continued_fractions_with_odd_period(10_000)


if __name__ == '__main__':
    Solution64().print_answer()
