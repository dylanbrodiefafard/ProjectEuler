from math import comb

from solutions.SolutionBase import SolutionBase


class Solution53(SolutionBase):
    NUMBER = 53
    VERIFIED_ANSWER = 4075

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        count = 0
        for n in range(1, 101):
            for r in range(1, n + 1):
                if comb(n, r) > 1000000:
                    count += 1
        return count


if __name__ == '__main__':
    Solution53().print_answer()
