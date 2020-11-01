from solutions.SolutionBase import SolutionBase


class P52(SolutionBase):
    NUMBER = 52
    VERIFIED_ANSWER = 142857

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        n = 1
        while True:
            digits = sorted(str(n))
            if (
                digits == sorted(str(2 * n)) and
                digits == sorted(str(3 * n)) and
                digits == sorted(str(4 * n)) and
                digits == sorted(str(5 * n)) and
                digits == sorted(str(6 * n))
            ):
                return n
            n += 1


if __name__ == '__main__':
    P52().print_answer()
