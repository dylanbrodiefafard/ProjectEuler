from solutions.SolutionBase import SolutionBase
from util.integers import num_partitions


class Solution76(SolutionBase):
    NUMBER = 76
    VERIFIED_ANSWER = 190569291

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        return num_partitions(100) - 1


if __name__ == '__main__':
    Solution76().print_answer()
