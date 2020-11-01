from solutions.SolutionBase import SolutionBase
from util.integers import num_divisors
from util.sequences import triangular


class Solution12(SolutionBase):
    NUMBER = 12
    VERIFIED_ANSWER = 76576500

    def run_tests(self, test_case):
        test_case.assertEqual(1, self.first_triangle_number_over_divisors(0))
        test_case.assertEqual(3, self.first_triangle_number_over_divisors(1))
        test_case.assertEqual(6, self.first_triangle_number_over_divisors(2))
        test_case.assertEqual(6, self.first_triangle_number_over_divisors(3))
        test_case.assertEqual(28, self.first_triangle_number_over_divisors(5))

    @staticmethod
    def first_triangle_number_over_divisors(n):
        for triangle in triangular():
            if num_divisors(triangle) > n:
                return triangle

    def get_answer(self):
        return self.first_triangle_number_over_divisors(500)


if __name__ == '__main__':
    Solution12().print_answer()
