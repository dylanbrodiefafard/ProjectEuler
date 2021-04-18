from solutions.SolutionBase import SolutionBase
from util.integers import is_square, NEGATIVE_INFINITY, continued_fraction_convergents, sqrt_continued_fraction


class Solution66(SolutionBase):
    NUMBER = 66
    VERIFIED_ANSWER = 661

    def run_tests(self, test_case):
        test_case.assertEqual(5, self.get_d_for_maximum_minimal_x(7))

    @staticmethod
    def get_d_for_maximum_minimal_x(maximum_d):
        d_max_x, max_x = None, NEGATIVE_INFINITY
        # Find the minimal solution to the equation x2 - Dy2 = 1
        for d in range(2, maximum_d + 1):
            if is_square(d):
                # assumed that there are no solutions in positive integers when D is square.
                continue
            for h, k in continued_fraction_convergents(sqrt_continued_fraction(d)):
                if h * h - d * k * k == 1:
                    if h > max_x:
                        d_max_x, max_x = d, h
                    break
        return d_max_x

    def get_answer(self):
        return self.get_d_for_maximum_minimal_x(1000)


if __name__ == '__main__':
    Solution66().print_answer()
