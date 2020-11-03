from itertools import product
from math import gcd

from solutions.SolutionBase import SolutionBase


class Solution33(SolutionBase):
    NUMBER = 33
    VERIFIED_ANSWER = 100

    def run_tests(self, test_case):
        test_case.assertTrue(self.is_curious_fraction(49, 98))
        test_case.assertFalse(self.is_curious_fraction(30, 50))

    @staticmethod
    def is_curious_fraction(numerator, denominator):
        num0, num1 = str(numerator)
        den0, den1 = str(denominator)
        if num1 == '0' and den1 == '0':
            return False  # trivial fraction
        value = numerator / denominator
        for num_i, den_i in product((0, 1), (0, 1)):
            num_cancel, num_left = (num0, num1) if num_i == 0 else (num1, num0)
            den_cancel, den_left = (den0, den1) if den_i == 0 else (den1, den0)
            if den_left == '0' or num_left == '0':
                continue  # division by 0 or 0 value fraction
            if num_cancel == den_cancel and (int(num_left) / int(den_left)) == value:
                return True
        return False

    def get_answer(self):
        numerator_product = denominator_product = 1
        for numerator in range(11, 100):
            for denominator in range(numerator + 1, 100):
                if not self.is_curious_fraction(numerator, denominator):
                    continue
                numerator_product *= numerator
                denominator_product *= denominator
        d = gcd(numerator_product, denominator_product)
        return denominator_product // d


if __name__ == '__main__':
    Solution33().print_answer()
