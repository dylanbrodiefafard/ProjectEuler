from collections import namedtuple
from math import gcd, floor

from solutions.SolutionBase import SolutionBase
from util.integers import POSITIVE_INFINITY


class Solution71(SolutionBase):
    NUMBER = 71
    VERIFIED_ANSWER = 428570

    def run_tests(self, test_case):
        test_case.assertTupleEqual((2, 5), self.fraction_to_left((3, 7), 8))

    @staticmethod
    def fraction_to_left(fraction, max_denominator):
        numerator, denominator = fraction
        assert denominator <= max_denominator
        assert numerator <= denominator

        value = numerator / denominator
        Answer = namedtuple('Answer', ['fraction', 'difference'])
        answer = Answer((0, 0), POSITIVE_INFINITY)

        for candidate_denominator in range(1, max_denominator + 1):
            if candidate_denominator == denominator:
                continue

            candidate_numerator = int(floor(value * candidate_denominator))
            assert candidate_numerator < candidate_denominator

            if gcd(candidate_numerator, candidate_denominator) != 1:
                continue  # not a reduced proper fraction

            difference = abs(candidate_numerator / candidate_denominator - value)
            if difference < answer.difference:
                answer = Answer((candidate_numerator, candidate_denominator), difference)
        return answer.fraction

    def get_answer(self):
        return self.fraction_to_left((3, 7), 1000000)[0]


if __name__ == '__main__':
    Solution71().print_answer()
