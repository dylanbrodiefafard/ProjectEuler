from solutions.BaseSolution import BaseSolution
from util.integers import multiplicative_order
from util.primes import primes


class Solution26(BaseSolution):
    NUMBER = 26
    VERIFIED_ANSWER = 983

    def run_tests(self, test_case):
        test_case.assertIsNone(self.denominator_with_longest_repetend(1))
        test_case.assertIsNone(self.denominator_with_longest_repetend(2))
        test_case.assertEqual(3, self.denominator_with_longest_repetend(3))
        test_case.assertEqual(3, self.denominator_with_longest_repetend(4))
        test_case.assertEqual(3, self.denominator_with_longest_repetend(5))
        test_case.assertEqual(7, self.denominator_with_longest_repetend(7))
        test_case.assertEqual(7, self.denominator_with_longest_repetend(8))
        test_case.assertEqual(7, self.denominator_with_longest_repetend(9))
        test_case.assertEqual(7, self.denominator_with_longest_repetend(10))

    @staticmethod
    def denominator_with_longest_repetend(max_denominator):
        denominator = None  # (length of recurring cycle, denominator)
        max_repetend_length = 0
        for p in primes():
            if p == 2 or p == 5:
                # coprime to 10
                continue
            if p > max_denominator:
                break
            repetend_length = multiplicative_order(10, p)
            if repetend_length > max_repetend_length:
                max_repetend_length = repetend_length
                denominator = p
        return denominator

    def get_answer(self):
        """
        From Wikipedia:
        A fraction in lowest terms with a prime denominator other than 2 or 5
        (i.e. coprime to 10) always produces a repeating decimal. The length of
        the repetend (period of the repeating decimal) of 1/p is equal to the order
        of 10 modulo p.
        """
        return self.denominator_with_longest_repetend(999)


if __name__ == '__main__':
    Solution26().print_answer()
