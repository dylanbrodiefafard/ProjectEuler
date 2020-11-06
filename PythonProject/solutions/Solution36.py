from solutions.SolutionBase import SolutionBase
from util.integers import is_palindrome


class Solution36(SolutionBase):
    NUMBER = 36
    VERIFIED_ANSWER = 872187

    def run_tests(self, test_case):
        test_case.assertListEqual([1, 3, 5, 7, 9], list(self.palindromes_in_base_10_and_2(20)))
        test_case.assertListEqual([1, 3, 5, 7, 9, 33, 99, 313, 585], list(self.palindromes_in_base_10_and_2(600)))

    @staticmethod
    def palindromes_in_base_10_and_2(up_to: int):
        for number in range(1, up_to + 1):
            if is_palindrome(number) and is_palindrome(int(str(bin(number))[2:])):
                yield number

    def get_answer(self):
        return sum(self.palindromes_in_base_10_and_2(1000000))


if __name__ == '__main__':
    Solution36().print_answer()
