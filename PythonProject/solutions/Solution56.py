from solutions.SolutionBase import SolutionBase
from util.integers import digital_sum


class P56(SolutionBase):
    NUMBER = 56
    VERIFIED_ANSWER = 972

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        max_digital_sum = 0
        for a in range(100):
            for b in range(100):
                max_digital_sum = max(max_digital_sum, digital_sum(a ** b))
        return max_digital_sum


if __name__ == '__main__':
    P56().print_answer()
