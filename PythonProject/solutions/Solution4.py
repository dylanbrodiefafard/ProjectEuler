from solutions.BaseSolution import BaseSolution
from util.integers import is_palindrome


class Solution4(BaseSolution):
    NUMBER = 4
    VERIFIED_ANSWER = 906609

    def run_tests(self, test_case):
        test_case.assertTrue(is_palindrome(91 * 99))

    def get_answer(self):
        for x in range(999, 900, -1):
            for y in range(999, 900, -1):
                if is_palindrome(x * y):
                    return x * y


if __name__ == '__main__':
    Solution4().print_answer()
