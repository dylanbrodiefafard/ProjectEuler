from itertools import takewhile

from solutions.SolutionBase import SolutionBase
from util.sequences import abundant


class Solution23(SolutionBase):
    NUMBER = 23
    VERIFIED_ANSWER = 4179871

    def run_tests(self, test_case):
        test_case.assertSetEqual(set(range(24)), self.positive_integers_cannot_be_written_as_sum_of_abundant_numbers(24))

    @staticmethod
    def positive_integers_cannot_be_written_as_sum_of_abundant_numbers(max_value: int):
        positive_integers = set(range(max_value + 1))
        abundant_numbers = list(takewhile(lambda n: n <= (max_value - 12), abundant()))
        num_abundant = len(abundant_numbers)
        for i, n_i in enumerate(abundant_numbers):
            if n_i // 2 > max_value:
                break
            for j in range(i, num_abundant):
                if (s := n_i + abundant_numbers[j]) > max_value:
                    break
                positive_integers.discard(s)
        return positive_integers

    def get_answer(self):
        return sum(self.positive_integers_cannot_be_written_as_sum_of_abundant_numbers(28123))


if __name__ == '__main__':
    Solution23().print_answer()
