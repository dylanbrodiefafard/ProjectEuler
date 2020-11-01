from math import log, ceil

from solutions.SolutionBase import SolutionBase


class Solution25(SolutionBase):
    NUMBER = 25
    VERIFIED_ANSWER = 4782
    PHI = 1.618033988749894848204586834365638117720309179805762862135448622705

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        return ceil(log(10) / log(self.PHI) * (log(5 ** .5, 10) + 999))


if __name__ == '__main__':
    Solution25().print_answer()
