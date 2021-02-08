from itertools import combinations_with_replacement

from solutions.SolutionBase import SolutionBase
from util.integers import num_proper_permutations_of_digits


class Solution92(SolutionBase):
    NUMBER = 92
    VERIFIED_ANSWER = 8581146
    POSSIBLE_DIGITS = list(map(str, range(10)))

    def run_tests(self, test_case):
        test_case.assertEqual(1, self.square_digit_chain_end(44))
        test_case.assertEqual(89, self.square_digit_chain_end(85))
        test_case.assertEqual(89, self.square_digit_chain_end(89))

    @staticmethod
    def square_digit_chain_end(n):
        while not (n == 1 or n == 89):
            n = sum(int(digit) ** 2 for digit in str(n))
        return n

    def get_answer(self):
        answer = 0
        for num_digits in range(1, 8):
            for digits in combinations_with_replacement(self.POSSIBLE_DIGITS, num_digits):
                n = int(''.join(digits))
                if n == 0 or self.square_digit_chain_end(n) != 89:
                    continue
                answer += num_proper_permutations_of_digits(digits, zero_value='0')
        return answer


if __name__ == '__main__':
    Solution92().print_answer()
