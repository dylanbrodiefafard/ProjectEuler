from solutions.SolutionBase import SolutionBase
from util.integers import pythagorean_triples


class Solution9(SolutionBase):
    NUMBER = 9
    VERIFIED_ANSWER = 31875000

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        for a, b, c in pythagorean_triples(1000):
            if a + b + c == 1000:
                return a * b * c


if __name__ == '__main__':
    Solution9().print_answer()
