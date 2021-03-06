from collections import namedtuple

from solutions.SolutionBase import SolutionBase
from util.integers import multiplicative_order
from util.sequences import prime_numbers_up_to


class Solution26(SolutionBase):
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
        Answer = namedtuple('Answer', ['denominator', 'repetend_length'])
        answer = Answer(None, 0)
        for p in prime_numbers_up_to(max_denominator):
            if p == 2 or p == 5:
                # coprime to 10
                continue
            repetend_length = multiplicative_order(10, p)
            if repetend_length > answer.repetend_length:
                answer = Answer(p, repetend_length)
        return answer.denominator

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
