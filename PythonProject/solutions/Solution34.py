from solutions.SolutionBase import SolutionBase
from util.integers import factorial


class Solution34(SolutionBase):
    NUMBER = 34
    VERIFIED_ANSWER = 40730
    """
    You need at least two digits to continue a sum, so the minimum number we
    should check is 10.

    Since there are only 10 digits in base 10, we can look at each of their
    factorials to see what kind of limits there are in this problem.

    9! = 362,880
    8! = 40,320
    7! = 5,040
    6! = 720
    5! = 120
    4! = 24
    3! = 6
    2! = 2
    1! = 1
    0! = 1

    If you look at the number of each of the digits of the factorials, you can
    see the maximum is 6 (9!) and if you add any of them up it doesn't change
    the number of digits of the sum. Therefore, the largest number we may have
    to check is 999,999 (the largest 6 digit number). However, if you look at
    the total sum of each of the factorials it is only 409,113. Since this
    number is relatively small, the easiest solution would be to check each
    number from 10 to 409,113.
    """

    def run_tests(self, test_case):
        test_case.assertEqual([145], list(self.numbers_equal_to_sum_of_factorial_of_digits(145)))
        test_case.assertEqual([145, 40585], list(self.numbers_equal_to_sum_of_factorial_of_digits(40585)))

    @staticmethod
    def numbers_equal_to_sum_of_factorial_of_digits(max_number):
        factorial_by_digit = {str(d): factorial(d) for d in range(0, 10)}

        for n in range(10, max_number + 1):
            if n == sum(map(factorial_by_digit.get, str(n))):
                yield n

    def get_answer(self):
        return sum(self.numbers_equal_to_sum_of_factorial_of_digits(409113))


if __name__ == '__main__':
    Solution34().print_answer()
