from math import gcd

from solutions.SolutionBase import SolutionBase
from util.integers import positive_divisors, moebius


class Solution73(SolutionBase):
    NUMBER = 73
    VERIFIED_ANSWER = 7295372

    def run_tests(self, test_case):
        test_case.assertEqual(0, self.num_proper_fractions_less_than(1, 8, 8))
        test_case.assertEqual(1, self.num_proper_fractions_less_than(1, 7, 8))
        test_case.assertEqual(2, self.num_proper_fractions_less_than(1, 6, 8))
        test_case.assertEqual(3, self.num_proper_fractions_less_than(1, 5, 8))
        test_case.assertEqual(4, self.num_proper_fractions_less_than(1, 4, 8))
        test_case.assertEqual(5, self.num_proper_fractions_less_than(2, 7, 8))
        test_case.assertEqual(6, self.num_proper_fractions_less_than(1, 3, 8))
        test_case.assertEqual(7, self.num_proper_fractions_less_than(3, 8, 8))
        test_case.assertEqual(8, self.num_proper_fractions_less_than(2, 5, 8))
        test_case.assertEqual(9, self.num_proper_fractions_less_than(3, 7, 8))
        test_case.assertEqual(10, self.num_proper_fractions_less_than(1, 2, 8))
        test_case.assertEqual(11, self.num_proper_fractions_less_than(4, 7, 8))
        test_case.assertEqual(12, self.num_proper_fractions_less_than(3, 5, 8))
        test_case.assertEqual(13, self.num_proper_fractions_less_than(5, 8, 8))
        test_case.assertEqual(14, self.num_proper_fractions_less_than(2, 3, 8))
        test_case.assertEqual(15, self.num_proper_fractions_less_than(5, 7, 8))
        test_case.assertEqual(16, self.num_proper_fractions_less_than(3, 4, 8))
        test_case.assertEqual(17, self.num_proper_fractions_less_than(4, 5, 8))
        test_case.assertEqual(18, self.num_proper_fractions_less_than(5, 6, 8))
        test_case.assertEqual(19, self.num_proper_fractions_less_than(6, 7, 8))
        test_case.assertEqual(20, self.num_proper_fractions_less_than(7, 8, 8))

    @staticmethod
    def num_coprime_up_to(n, up_to):
        num_coprime = 0
        for d in positive_divisors(n):
            num_coprime += moebius(d) * (up_to // d)
        return num_coprime

    @staticmethod
    def num_proper_fractions_less_than(numerator, denominator, max_denominator):
        assert numerator < denominator
        assert gcd(numerator, denominator) == 1

        value = numerator / denominator
        num_less_than = 0
        for d in range(2, max_denominator + 1):
            if denominator == d:
                n = numerator - 1
            else:
                n = int(value * d)
            num_less_than += Solution73.num_coprime_up_to(d, n)
        return num_less_than

    def get_answer(self):
        return self.num_proper_fractions_less_than(1, 2, 12000) - (1 + self.num_proper_fractions_less_than(1, 3, 12000))


if __name__ == '__main__':
    Solution73().print_answer()
