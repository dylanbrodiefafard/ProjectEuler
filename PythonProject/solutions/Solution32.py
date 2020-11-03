from collections import Counter
from itertools import islice

from solutions.SolutionBase import SolutionBase
from util.integers import proper_factors


class Solution32(SolutionBase):
    NUMBER = 32
    VERIFIED_ANSWER = 45228

    def run_tests(self, test_case):
        test_case.assertEqual([(39, 186)], list(self.pandigital_factors(7254)))

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
        # Only need to zip half of the factors, because the second half would be the same factors,
        # but in a different order; i.e., a * b and b * a.
        # These produce the same product, so we only need one pair.
        half_index = -(len(factors) // -2)  # use double negative to perform ceiling integer division
        for multiplicand, multiplier in islice(zip(factors, reversed(factors)), half_index):
            if multiplier * multiplicand != product:
                continue  # identity doesn't hold
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
