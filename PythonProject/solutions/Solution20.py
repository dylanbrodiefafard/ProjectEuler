from solutions.BaseSolution import BaseSolution
from util.integers import digital_sum, factorial


class Solution20(BaseSolution):
    NUMBER = 20
    VERIFIED_ANSWER = 648

    def run_tests(self, test_case):
        test_case.assertEqual(27, self.digital_sum_of_factorial(10))

    @staticmethod
    def digital_sum_of_factorial(n):
        return digital_sum(factorial(n))

    def get_answer(self):
        return self.digital_sum_of_factorial(100)


if __name__ == '__main__':
    Solution20().print_answer()
