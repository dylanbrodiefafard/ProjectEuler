from solutions.SolutionBase import SolutionBase
from util.integers import digital_sum


class Solution16(SolutionBase):
    NUMBER = 16
    VERIFIED_ANSWER = 1366

    def run_tests(self, test_case):
        test_case.assertEqual(26, digital_sum(2 ** 15))

    def get_answer(self):
        return digital_sum(2 ** 1000)


if __name__ == '__main__':
    Solution16().print_answer()
