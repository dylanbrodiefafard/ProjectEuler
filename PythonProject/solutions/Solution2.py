from solutions.SolutionBase import SolutionBase


class Solution2(SolutionBase):
    NUMBER = 2
    VERIFIED_ANSWER = 4613732

    def run_tests(self, test_case):
        pass

    def get_answer(self):
        sum_of_even_fibonacci_terms = 0
        term1 = 0
        term2 = 1

        while term2 < 4000001:
            if term2 % 2 == 0:
                sum_of_even_fibonacci_terms += term2
            term1, term2 = term2, term1 + term2
        return sum_of_even_fibonacci_terms


if __name__ == '__main__':
    Solution2().print_answer()
