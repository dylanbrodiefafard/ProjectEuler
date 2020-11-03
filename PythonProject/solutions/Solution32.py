from collections import Counter

from solutions.SolutionBase import SolutionBase
from util.integers import proper_factors


class Solution32(SolutionBase):
    NUMBER = 32
    VERIFIED_ANSWER = 45228

    def run_tests(self, test_case):
        test_case.assertEqual([(39, 186), (186, 39)], list(self.pandigital_factors(7254)))

    @staticmethod
    def pandigital_factors(product):
        # Yields all multiplicand/multiplier pairs that equal the product where
        # the numbers 1 through 9 are used only once in all multiplicand/multiplier/product
        if '0' in (product_digits := str(product)):
            return  # Exit early when we have a zero in the number.
        if len(product_digit_counts := Counter(product_digits)) != len(product_digits):
            return  # Return early when the product has duplicate digits (cannot be pandigital)
        factors = proper_factors(product)[1:]  # Ignore the '1' factor for every number
        if not factors:
            return  # prime
        for multiplicand, multiplier in zip(factors, reversed(factors)):
            if '0' in (multiplicand_digits := str(multiplicand)):
                continue  # zero not allowed
            if '0' in (multiplier_digits := str(multiplier)):
                continue  # zero not allowed
            identity_digit_counts = Counter(multiplicand_digits + multiplier_digits)
            identity_digit_counts.update(product_digit_counts)
            if len(identity_digit_counts) == 9:
                # the entire identity is pandigital. yield it!
                yield multiplicand, multiplier

    def get_answer(self):
        return sum(
            n for n in range(1000, 9999)
            if next(self.pandigital_factors(n), None) is not None
        )


if __name__ == '__main__':
    Solution32().print_answer()
